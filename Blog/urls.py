
from django.urls import path 
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blog', home ,name='homepage'),
    path('blog/<str:pk>',article , name = 'article'),
    path('edit/<str:pk>' , edit, name= 'editpage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
