from .settings import ALLOWED_IP
from django.http import HttpResponseForbidden

class IPRestrictionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        allowed_ip = ALLOWED_IP
        print(allowed_ip)
        ip = request.META.get('REMOTE_ADDR')
        print(ip)
        if ip != allowed_ip:
            return HttpResponseForbidden("Access Denied: Your IP address is not allowed.")
        return self.get_response(request)
