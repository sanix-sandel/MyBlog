from django.urls import path
from . import views

urlpatterns = [
    path('all', views.all_files),
   # path('<int:id>', views.file_detail),
   # path('<str:by_tag>', views.files_by_tag),
]
