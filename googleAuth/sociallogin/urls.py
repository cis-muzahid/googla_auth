from django.urls import path
from . import views

urlpatterns = [
      path('auth/google-login/', views.GoogleLoginApi.as_view(), name='google-login'),



]