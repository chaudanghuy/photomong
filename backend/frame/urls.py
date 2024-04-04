from django.urls import path, include
from .views import (
    FrameAPI,
    FrameDetailAPI,
    FrameList,
    FrameCreateView,
    FrameEditView,
    FrameImageCopyAPI,    
)
from .views import upload_full

urlpatterns = [
    # API
    path('api', FrameAPI.as_view()),
    path('api/<int:pk>', FrameDetailAPI.as_view()),
    # API Image
    path('api/copy-image', FrameImageCopyAPI.as_view()),
    path('api/upload-full', upload_full, name='upload-full'),
    # WEB
    path('', FrameList.as_view(), name='frames'),
    path('add', FrameCreateView.as_view(), name='frames-add'),
    path('edit/<int:pk>', FrameEditView.as_view(), name='frames-edit')
]