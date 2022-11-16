import datetime

from pytz import timezone

from config import settings
from config.celery import app
from django.core.mail import send_mail

from mail.models import Mailings
from users.models import SubLists, Subscribers
from templates.models import MailingTemplates


@app.task
def ActualMailing(id_mailing: int) -> bool:
    """Рассылка выбранного макета по подписчикам в выбранном списке рассылки"""
    mailing = Mailings.objects.get(id=id_mailing)
    template = MailingTemplates.objects.get(id=mailing.template_id)
    sublist = SubLists.objects.get(id=mailing.sublist_id)
    for sub in sublist.subscribers.all():
        sub_html = template.html
        for jinja in ['{{ surname }}', '{{ name }}', '{{ birthday }}']:
            if jinja in sub_html:
                field_object = Subscribers._meta.get_field(jinja[3:-3])
                field_value = getattr(sub, field_object.attname)
                if jinja == '{{ birthday }}':
                    sub_html = sub_html.replace(jinja, field_value.strftime('%d.%m.%Y'))
                else:
                    sub_html = sub_html.replace(jinja, field_value)
        sub_html += sub_html + '<img src="http://'+settings.PROJECT_URL+'/tracking/'+str(mailing.id)+'/'+sub.email+'/">'
        send_mail(
            mailing.name,
            '',
            None,
            [sub.email,],
            fail_silently=False,
            html_message=sub_html
        )
    mailing.complete = True
    mailing.save()
    return True


@app.task
def CheckTimeOfMailings() -> bool:
    """Проверка на наличие отложенных рассылок с подходящим временем для выполнения"""
    for mailing in Mailings.objects.all():
        if mailing.now is False:
            settings_time_zone = timezone(settings.TIME_ZONE)
            if mailing.time_mail <= datetime.datetime.now().astimezone(settings_time_zone):
                if mailing.complete is False:
                    ActualMailing(mailing.id)
    return True
