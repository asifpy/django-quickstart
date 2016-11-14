from django.dispatch import receiver
from crudbuilder.signals import(
    post_create_signal,
    post_update_signal,
    post_inline_create_signal,
    post_inline_update_signal
)

from core.models import Post


@receiver(post_create_signal, sender=Post)
def post_create_signal_handler(sender, **kwargs):
    request = kwargs['request']
    instance = kwargs['instance']

    instance.created_by = request.user
    instance.save()


@receiver(post_update_signal, sender=Post)
def post_update_signal_handler(sender, **kwargs):
    request = kwargs['request']
    instance = kwargs['instance']

    instance.updated_by = request.user
    instance.save()