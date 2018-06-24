from django.conf.urls import url

from .views import VideoUploadView, get_all_video

urlpatterns = [
    url(r'^upload$', VideoUploadView.as_view(), name='file-upload'),
    url(r'^$', get_all_video),
]
