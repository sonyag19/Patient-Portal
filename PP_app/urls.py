from django.urls import path
from .views import *

urlpatterns=[
    path('Navbar/',Navbar),
    path('Footer/',Footer),
    path('Index/',Index),
    # path('Login/',Login),
    path('login/',Login.as_view(),name='login'),
    # path('SignUp/',SignUp)
    path('register/',SignUp.as_view(),name='register'),
    path('profile/',Profile),
    path('edit_profile/<int:id>',edit_profile),
    path('loginAll/',LoginAll),
    path('home/<int:id>',home),
    path('newAppointment/',newApptClass.as_view(),name='newAppointment'),
    path('visits/',visits)


]