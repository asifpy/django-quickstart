from django.apps import AppConfig


class AddAnotherExampleConfig(AppConfig):
    name = 'addanother_example'

    def ready(self):
        from . import handlers
