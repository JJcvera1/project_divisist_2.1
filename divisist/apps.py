from django.apps import AppConfig


class DivisistConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'divisist'

    def ready(self):
        import divisist.signals 