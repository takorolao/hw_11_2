from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homework/', include('hw_11_10app.urls')), 
]

