from django.contrib import admin
from .models import all_classes


def register_models():
    """
    Register all models from the 'all_classes' list with the Django admin site.

    This function iterates through the list of model classes defined in 'all_classes' and registers
    each of them with the Django admin site, making them accessible for administration.

    Returns:
        None
    """
    for i in all_classes:
        admin.site.register(i)


# Call the function to register the models
register_models()
