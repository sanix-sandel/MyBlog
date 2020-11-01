from django.urls import path

urlpatterns = [
    path('all', views.all_posts),
    path('<int:id>', views.post_detail),
    path('<str:by_tag>', views.files_by_tag),
]
