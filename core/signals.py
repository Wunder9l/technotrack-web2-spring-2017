from django.db import transaction
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from application import settings
from core.models import WatchableModel, User
from event.models import add_event_for_object
from .models import ModelWithAuthor, Like
from .tasks import send_confirmation_email_task


# transaction.on_commit(lambda: dewfewhfwe)

def model_with_author_post_save(instance, created=False, *args, **kwargs):
    if created:
        instance.author.objects_count += 1
        instance.author.save()


@receiver(post_save, sender=Like)
def like_post_save(instance, created, *args, **kwargs):
    if created:
        instance.object.likes_count += 1
        instance.object.save()


@receiver(pre_delete, sender=Like)
def like_pre_delete(instance, *args, **kwargs):
    instance.object.likes_count -= 1
    if 0 > instance.object.likes_count:
        instance.object.likes_count = 0
    instance.object.save()


def watchable_object_post_save(instance, created, *args, **kwargs):
    if instance.is_tracked():
        # we create new event on each object edit
        add_event_for_object(instance, created=created)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=User)
def confirm_user_email(instance, created, *args, **kwargs):
    if created:
        transaction.on_commit(lambda: send_confirmation_email_task.apply_async([instance.id], {}))


# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)

for model in WatchableModel.__subclasses__():
    post_save.connect(watchable_object_post_save, model)

for model in ModelWithAuthor.__subclasses__():
    post_save.connect(model_with_author_post_save, model)

# post_save.connect()
# for model in WatchableModel.__subclasses__():
# post_save.connect(m)
