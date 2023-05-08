from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView


urlpatterns = [
    path('', SpectacularSwaggerView.as_view(url_name='schema')),
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('api/card/', include('card.urls', namespace='card')),
    path('api/question/', include('question.urls', namespace='question')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
]
