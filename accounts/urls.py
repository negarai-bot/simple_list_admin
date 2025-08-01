
from django.urls import path
from . import views
urlpatterns = [
    path('', views.Signupview.as_view(), name='signup'),
]
