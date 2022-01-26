from django.urls import path
from .views import home, sendmail

urlpatterns = [
    path('', home, name='home' ),
    path('sendmail', sendmail, name='sendmail')


]
