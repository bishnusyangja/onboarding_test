from django.contrib.auth.models import User

from django.conf import settings


class DefaultLoginUserMiddleware:

    def get_default_user(self):
        try:
            user = User.objects.filter(email=settings.DEFAULT_MIDDLEWARE_USER_EMAIL).first()
        except User.DoesNotExist:
            user = User.objects.first()
        return user

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.user = self.get_default_user()
        # Code to be executed for each request before the view (and later middleware) are called
        response = self.get_response(request)
        # Code to be executed for each response before it's returned to the client
        return response
