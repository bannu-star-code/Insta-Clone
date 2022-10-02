from django.contrib import admin
from django.urls import path,include
# to add media root 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('authentication.urls')),
    path('', include('core.urls')),
    path('', include('user.urls')),
]

if settings.DEBUG == True:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)