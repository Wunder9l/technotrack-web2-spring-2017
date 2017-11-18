from datetime import timedelta
from django.utils import timezone
from celery import shared_task
from celery.task import periodic_task
from celery.schedules import crontab
from core.constants import DIGEST_PERIOD, DIGEST_MAX_ENTRY
from event.models import Event
from .mail import send_confirm_email, send_digest_email
from .models import User


# @task(bind=True)
# def send_confirmation_email_task(self, user_id)
@shared_task()
def send_confirmation_email_task(user_id):
    user = User.objects.get(id=user_id)
    if user:
        send_confirm_email(user, user.email)


@shared_task()
def send_digest(user_id):
    user = User.objects.get(id=user_id)
    if user and not user.is_digest_sent():
        following = list(user.get_following().values_list('id', flat=True))
        events = Event.objects.filter(user_id__in=following).prefetch_related('object')
        # events = events.filter(updated__gt=timezone.now() - DIGEST_PERIOD).order_by('-updated')
        events = events[:DIGEST_MAX_ENTRY]
        if len(events) > 0:
            send_digest_email(user, [e.object.get_title_for_event(e.type) for e in events if e.object])
            user.last_digest_sent = timezone.now()
            user.save(update_fields=["last_digest_sent"])


@periodic_task(run_every=crontab(minute="*"))  # hour=20
def digest_dispatch():
    for user_id in User.objects.values_list('id', flat=True).all():
        send_digest.apply_async([user_id], {})


@shared_task()
def test(n):
    return n ** 100
