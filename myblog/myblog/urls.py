
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('files/', include('files.urls')),
    path('posts/', include('posts.urls')),
]
