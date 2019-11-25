from django.apps import AppConfig


class EvalhubappConfig(AppConfig):
    name = 'evalhubapp'
    verbose_name = 'EvalHub'

    def ready(self):
        import evalhubapp.signals
