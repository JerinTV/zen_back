from django.db import OperationalError
from django.http import JsonResponse


class DatabaseErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except OperationalError:
            if request.path.startswith("/api/"):
                return JsonResponse(
                    {
                        "detail": (
                            "Database is not configured or is unreachable. "
                            "Set DATABASE_URL or MYSQL_URL in the backend deployment."
                        )
                    },
                    status=503,
                )
            raise
