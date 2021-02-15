from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='EMS API Documentation')
# Adding path to different end points.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('form.urls', namespace='form')),
    path('memes/', include('form_api.urls', namespace='form_api')),
    path('swagger-ui/',schema_view),
]

