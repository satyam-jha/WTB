
from django.urls import path 
from .views import *

urlpatterns = [
    path('blog', home ,name='homepage'),
    path('blog/<str:pk>',article , name = 'article'),
    path('edit/<str:pk>' , edit, name= 'editpage')
]
