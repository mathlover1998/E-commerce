from django.apps import AppConfig


class AuthCartConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authcart'

    # def ready(self):
    #     import authcart.signals