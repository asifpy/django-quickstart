from django.apps import AppConfig


class CrudbuilderExampleConfig(AppConfig):
    name = 'crudbuilder_example'

    def ready(self):
        from . import handlers
