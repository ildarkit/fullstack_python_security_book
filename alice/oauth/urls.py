from django.urls import path
from . import views


urlpatterns = [
    path('hello/', views.ScopedEmailView.as_view(), name='oauth'),
]
