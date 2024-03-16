from django.urls import path, include
from .views import (
     StickerAPI,
     StickerDetailAPI,
     StickerList,
     StickerCreateView,
     StickerEditView
)

urlpatterns = [
      # API
      path('api', StickerAPI.as_view()),
      path('api/<int:pk>', StickerDetailAPI.as_view()),
      # WEB
      path('', StickerList.as_view(), name='stickers'),
      path('add', StickerCreateView.as_view(), name='sticker-add'),
      path('edit/<int:pk>', StickerEditView.as_view(), name='sticker-edit')          
  ]