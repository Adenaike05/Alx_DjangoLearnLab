from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = "accounts"

    def ready(self):
        from django.contrib.auth import get_user_model

        User = get_user_model()
        # If you're importing signals or doing something with User, do it here
        # Example:
        # from . import signals
