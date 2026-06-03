# zentodo_backend/zentodo_backend/urls.py

from django.conf import settings
from django.contrib import admin
from django.http import HttpResponse, JsonResponse
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tasks.views import TodoViewSet, UserViewSet # <-- Keep this, for your tasks/users list/retrieve

# Import JWT refresh view (TokenObtainPairView is now handled by users.urls)
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    # TokenVerifyView, # Optional: if you want an endpoint to verify tokens
)

# Create a router for your ViewSets
router = DefaultRouter()
# Register your TodoViewSet.
router.register(r'tasks', TodoViewSet)
# Register your UserViewSet. This is for general user listing/detail, NOT registration.
router.register(r'users', UserViewSet, basename='user')


def root_view(_request):
    return JsonResponse(
        {
            "status": "ok",
            "service": "zentodo_backend",
            "database_configured": bool(settings.DATABASE_URL),
            "endpoints": {
                "api_root": "/api/",
                "admin": "/admin/",
            },
        }
    )


def favicon_view(_request):
    # Avoid noisy 404s in dev when hitting the backend directly in a browser.
    return HttpResponse(status=204)


urlpatterns = [
    path("", root_view, name="root"),
    path("favicon.ico", favicon_view, name="favicon"),

    # Django Admin Panel URL
    path('admin/', admin.site.urls),

    # Your main API routes (defined by the router)
    path('api/', include(router.urls)),

    # URLs from your 'users' app (includes /api/register/ and your custom /api/token/)
    path('api/', include('users.urls')), # <--- THIS IS THE NEW LINE YOU ADDED

    # JWT Authentication URLs
    # This endpoint allows clients to get a new access token using a refresh token
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Optional: Uncomment if you want an endpoint to verify if a token is valid
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Optional: DRF's browsable API login/logout
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
