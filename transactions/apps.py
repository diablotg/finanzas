from django.apps import AppConfig


class TransaccionesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "transactions"

    def ready(self):
        # Import the signals module to ensure the signal handlers are registered
        import transactions.signals  # noqa: F401

        # Import the models module to ensure the models are registere
