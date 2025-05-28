from django.contrib import admin
from django.urls import path
from django.urls import include
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('__debug__/', include("debug_toolbar.urls"))
] 
