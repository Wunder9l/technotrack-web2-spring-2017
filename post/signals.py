import os
from django.db.models.signals import post_save
from django.dispatch import receiver

from application.settings import MEDIA_ROOT
from core.utils import post_title_image_save_path
from .models import Post


@receiver(post_save, sender=Post)
def post_object_post_save(instance, created, *args, **kwargs):
    if created:
        new_filename = post_title_image_save_path(instance, instance.title_image.name)
        old_abs_path = os.path.join(MEDIA_ROOT, instance.title_image.name)
        print old_abs_path, os.path.isfile(old_abs_path)
        if os.path.isfile(old_abs_path):
            new_abs_path = os.path.join(MEDIA_ROOT, new_filename)
            os.renames(old_abs_path, new_abs_path)
            instance.title_image.name = new_filename
            instance.save(update_fields=["title_image"])
            # instance.object.title_image += 1
            # instance.object.save()
