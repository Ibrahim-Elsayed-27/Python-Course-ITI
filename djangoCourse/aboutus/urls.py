from django.urls import path
from aboutus.views import about_us

app_name = 'aboutus'

urlpatterns = [
    path('', about_us, name='about'),  # Change name to 'about'
]