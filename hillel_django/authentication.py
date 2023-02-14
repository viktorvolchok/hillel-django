from django.contrib.auth.models import User
from rest_framework.authentication import BaseAuthentication


class GloryToUkraineAuthentication(BaseAuthentication):
    def authenticate(self, request):
        query_params = request.GET

        if query_params.get("haslo") == "SlavaUkraini":
            return User.objects.get(username="vitaliipavliuk"), None
