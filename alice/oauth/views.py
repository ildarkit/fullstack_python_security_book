from django.http import JsonResponse
from oauth2_provider.views import ScopedProtectedResourceView


class ScopedEmailView(ScopedProtectedResourceView):
    required_scopes = ['email', ]

    def get(self, request):
        return JsonResponse({
            'email': request.user.email,
        })
