from django.contrib.auth.models import AnonymousUser
from rest_framework import authentication


class AnonymousAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        return (AnonymousUser(), None)
