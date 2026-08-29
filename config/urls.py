from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from django.utils import timezone

def root_overview(request):
    return JsonResponse({
        'status': 'success',
        'message': 'Welcome to GigFlow Django REST API & Admin Server',
        'version': '1.0.0 (Django Framework)',
        'endpoints': {
            'django_admin': '/admin/',
            'health': '/api/health',
            'items': '/api/items',
        }
    })

def health_check(request):
    return JsonResponse({
        'status': 'success',
        'message': 'GigFlow Django API is healthy and operational',
        'timestamp': timezone.now().isoformat(),
    })

urlpatterns = [
    path('', root_overview, name='root-overview'),
    path('admin/', admin.site.urls),
    path('api/health', health_check, name='health-check'),
    path('api/items', include('items.urls')),
    path('api/items/', include('items.urls')),
]
