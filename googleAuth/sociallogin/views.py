from urllib.parse import urlencode
from rest_framework import serializers
from rest_framework.views import APIView
from django.conf import settings
from django.shortcuts import redirect
from rest_framework.response import Response
from .mixins import PublicApiMixin, ApiErrorsMixin
from .utils import google_get_access_token, google_get_user_info, generate_tokens_for_user
from django.contrib.auth.models import User
from .serializers import UserSerializer
from googleAuth.settings import *
from django.core.exceptions import ValidationError


class GoogleLoginApi(PublicApiMixin, ApiErrorsMixin, APIView):
    """
    Custom Google login view.

    Handles Google OAuth2 authentication and generates JWT tokens for authenticated users.

    Attributes:
        InputSerializer: Serializer class for validating input data.
    """

    class InputSerializer(serializers.Serializer):
        """
        Serializer class for validating input data.
        """

        code = serializers.CharField(required=False)
        error = serializers.CharField(required=False)

    def get(self, request, *args, **kwargs):
        """
        Handle GET request for Google OAuth2 login.

        Args:
            request (Request): The request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: Response with user data and JWT tokens.
        """
        input_serializer = self.InputSerializer(data=request.GET)
        input_serializer.is_valid(raise_exception=True)

        validated_data = input_serializer.validated_data
        code = validated_data.get('code')
        error = validated_data.get('error')

        login_url = f'{settings.DASHBOARD_BASE_ROUTE}'
        if error or not code:
            params = urlencode({'error': error})
            return redirect(f'{login_url}?{params}')

        redirect_uri = f'{settings.GOOGLE_REDIRECT_URL}'
        access_token = google_get_access_token(code=code, redirect_uri=redirect_uri)
        user_data = google_get_user_info(access_token=access_token)

        try:
            user = User.objects.get(email=user_data['email'])
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
        except Exception as error:
            try:
                user = User.objects.create(
                    email=user_data['email'],
                    username=user_data['given_name'],
                    is_email_verified=user_data['email_verified'],
                    authentication_provider='Google',
                    is_active=True
                )
            except Exception as error:
                raise ValidationError('Failed to create user.') from error

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

        response_data = {
            'user': UserSerializer(user).data,
            'access_token': access_token,
            'refresh_token': refresh_token
        }
        print("response_data",response_data)

        return Response(response_data)

