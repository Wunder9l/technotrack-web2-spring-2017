from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import ModelWithAuthor, Like


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


for model in ModelWithAuthor.__subclasses__():
    post_save.connect(model_with_author_post_save, model)
