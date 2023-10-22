from django.urls import path, include
from .views import *

from . import REQ1 as req1

urlpatterns = [
    # REQ1
    #link for the request method "register" which will receive the credentials for a registre to be saved in the database
    path("register/", req1.register), 
    #link for the request method "login" which will receive the credentials for verification of the user registre in the database   
    path("login/", req1.login),

    #links for every possible option to be chosen by the user once logged in the app
    path("REQ2/", include("api.REQ2.urls")),
    path("REQ3/", include("api.REQ3.urls")),
    path("REQ4/", include("api.REQ4.urls")),
    path("REQ5/", include("api.REQ5.urls")),
    path("REQ6/", include("api.REQ6.urls")),
    path("REQ7/", include("api.REQ7.urls")),
    path("REQ8/", include("api.REQ8.urls")),
]
