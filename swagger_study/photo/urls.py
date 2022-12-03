from django.urls import path
from photo.views import PhotoView

urlpatterns = [
    path("photo", PhotoView.as_view())
]
