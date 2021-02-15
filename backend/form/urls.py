from django.urls import path
from django.views.generic import TemplateView

app_name = 'form'
#Rendering basic html to see if backend is working
urlpatterns = [
    path('', TemplateView.as_view(template_name="form/index.html")),
]
