from django.urls import path
from . import views
from .views import ImageUploadView

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', ImageUploadView.as_view(), name='image-upload'),
    path('uploadImg/', views.uploadImg, name='uploadImg'),
    path('listenAndRecognize/', views.listenAndRecognize, name='listenAndRecognize'),
    path('uploadFrame/', views.uploadFrame, name='uploadFrame'),
]
