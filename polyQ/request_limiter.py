from django.core.cache import cache
from datetime import datetime, timedelta
from django.http import HttpResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == "POST" and "form_submission" in request.path:
            ip = self.get_client_ip(request)
            key = f"rate_limit_{ip}"

            # Get the current time and expiration time
            now = datetime.now()
            request_count = cache.get(key, 0)
            expiration_time = cache.get(f"{key}_time", now)

            if now < expiration_time:
                if request_count >= 5:
                    # Exceeded rate limit
                    return HttpResponse('Too many requests. Please try again later.', status=429)

            # Allow request, update count and expiration
            if now >= expiration_time:
                cache.set(key, 1, timeout=60)  # Reset count if the time window expired
                cache.set(f"{key}_time", now + timedelta(minutes=1), timeout=60)
            else:
                cache.set(key, request_count + 1, timeout=60)

        # Continue processing the request if it's within the rate limit
        return self.get_response(request)

    def get_client_ip(self, request):
        """ Get the real IP address of the client from the request headers. """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip