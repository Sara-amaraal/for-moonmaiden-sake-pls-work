## Author

    João Macedo

# Test Scenario

    Test whether the "api" application settings have been well defined in the Django project.
        - application name;
        - default auto-increment field that will be used to create primary keys in the database tables associated with models in this application;

# Actions to take

     Navigate to the root directory of your Django project. This is the directory where the manage.py file is located. You open an interactive Django shell with the command "python manage.py shell" an then, execute the following commands:
        - from api.apps import ApiConfig
        - default_auto_field = ApiConfig.default_auto_field
        - app_name = ApiConfig.name
        - print(f"Default Auto Field: {default_auto_field}")
        - print(f"App Name: {app_name}")

# Expected Result

    The expected result will be the project settings defined in the apps.py file by the ApiConfig class.

# Observed Result

    The results observed were exactly the ones described in the 'Expected Result'.

# Success?

    Yes
