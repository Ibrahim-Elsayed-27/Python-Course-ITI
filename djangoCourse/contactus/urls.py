from django.urls import path
from contactus.views import contact_us

app_name = 'contactus'

urlpatterns = [
    path('', contact_us, name='contact'),  # Change name to 'contact'
]