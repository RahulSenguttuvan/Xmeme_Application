from django.urls import path
from .views import List_Create_FormData, Edit_Retrieve_FormData

app_name = 'form_api'
# Adding end point to create, list, retrieve and patch methods.
urlpatterns = [
    path('', List_Create_FormData.as_view(), name='listcreate'),
    path('<int:pk>/', Edit_Retrieve_FormData.as_view(), name='editFormData'),
]