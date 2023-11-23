from django.urls import path
from . import views


urlpatterns = [
    path('oauth/callback/', views.OAuthCallbackView.as_view()),
    path('welcome/', views.WelcomeView.as_view(), name='welcome'),
]
