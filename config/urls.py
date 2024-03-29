from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Test app API",
      default_version='v1',
      description="API for menu",
      terms_of_service="https://www.example.com/",
      contact=openapi.Contact(email="example@example.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0),
          name='schema-json'),
    re_path(r"^swagger/$", schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r"^redoc/$", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path(settings.ADMIN_URL, admin.site.urls),
    path("api/courses/", include("apps.courses.urls",  namespace="courses")),
    path("api/students/", include("apps.students.urls", namespace="students")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
