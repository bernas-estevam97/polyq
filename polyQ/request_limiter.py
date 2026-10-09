import logging

from django.core.cache import cache
from django.db import DatabaseError
from django.http import HttpResponse

logger = logging.getLogger(__name__)

# Feedback form POSTs go to the disease page URL (see templates/diseases.html).
RATE_LIMITED_PATHS = ('/disease_search/',)
MAX_REQUESTS = 5
WINDOW_SECONDS = 60


class RateLimitMiddleware:
    """Allow at most MAX_REQUESTS feedback submissions per IP per WINDOW_SECONDS."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and request.path.startswith(RATE_LIMITED_PATHS):
            try:
                if self.over_limit(request):
                    return HttpResponse('Too many requests. Please try again later.', status=429)
            except DatabaseError:
                # Cache unavailable (e.g. `manage.py createcachetable` never run): let the
                # request through rather than break the feedback form, and say why in the logs.
                logger.exception("Rate limiter cache unavailable; request not limited")

        return self.get_response(request)

    def over_limit(self, request):
        key = f"rate_limit_{self.get_client_ip(request)}"
        # add() only sets the key if missing, so the window starts at the first request
        if cache.add(key, 1, timeout=WINDOW_SECONDS):
            return False
        try:
            count = cache.incr(key)
        except ValueError:  # expired between add() and incr()
            cache.set(key, 1, timeout=WINDOW_SECONDS)
            count = 1
        return count > MAX_REQUESTS

    def get_client_ip(self, request):
        """Real client IP. Behind a proxy that appends to X-Forwarded-For (nginx
        $proxy_add_x_forwarded_for), the last entry is the one the proxy saw; the
        first entry is whatever the client sent and can be spoofed."""
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            return x_forwarded_for.split(',')[-1].strip()
        return request.META.get('REMOTE_ADDR')
