from django.apps import AppConfig


class AuthappConfig(AppConfig):
    name = 'authApp'

    def ready(self):
    	import authApp.signals
