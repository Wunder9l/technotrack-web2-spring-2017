from django.db.models.signals import post_save, post_init, pre_save, pre_delete
from django.dispatch import receiver
from comment.models import Comment


def comment_init(instance, *args, **kwargs):
    instance.text_was = instance.text


def comment_presave(instance, created=False, *args, **kwargs):
    # print "created", created, 'edited',instance.text != instance.text_was
    if not created and instance.text != instance.text_was:
        instance.text_was = instance.text
        instance.edited_count += 1


def comment_postsave(instance, created=False, *args, **kwargs):
    if created:
        instance.object.comments_count += 1
        instance.object.save()


@receiver(pre_delete, sender=Comment)
def comment_delete(instance, *args, **kwargs):
    instance.object.comments_count -= 1
    if 0 > instance.object.comments_count:
        instance.object.comments_count = 0
    instance.object.save()


post_save.connect(comment_postsave, Comment)
pre_save.connect(comment_presave, Comment)
post_init.connect(comment_init, Comment)
