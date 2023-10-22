from django.apps import AppConfig


class ApiConfig(AppConfig):
    """
    Configuration class for the API application.

    This class defines specific settings for the API application.

    Attributes:
        default_auto_field (str): The name of the default auto-increment field.
        name (str): The name of the application.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
