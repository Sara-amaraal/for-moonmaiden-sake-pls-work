## Author

    João Macedo

# Test Scenario

    Test if the model classes have been successfully registered in the Django admin site and are accessible in the admin interface.

# Actions to take

    - Run the Backend application server and follow the link provided. Once there, you must add the path to the website link through “/admin/”. Then you must log in to the admin interface with admin credentials.
    - If you don't know your admin credentials, you can create one. Navigate to the root directory of your Django project. This is the directory where the manage.py file is located. Run the following command "python manage.py createsuperuser" and so, create your superuser.

# Expected Result

    - In the administration interface, you should see the data models that were registered using the register_models() function. They will appear in the list of templates available for administration.
    - If you click on one of the models, you will be able to view and manage them, which confirms that the models have been registered successfully.

# Observed Result

    The results observed were exactly the ones described in the 'Expected Result'.

# Success?

    Yes
