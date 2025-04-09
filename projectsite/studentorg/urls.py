from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),         # URL for the admin panel
    path('', include('studentorg.urls')),   # Include URLs from the 'studentorg' app
]