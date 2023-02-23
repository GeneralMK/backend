from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view

schema_view= swagger_get_schema_view(
    openapi.Info(
        title="Rejufinate API Document",
        default_version="1.0.0",
        description="API GUIDE"
    ),
    public=True
)

urlpatterns = [
    path('swagger/',schema_view.with_ui('swagger', cache_timeout=0),name="api_schema"),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
