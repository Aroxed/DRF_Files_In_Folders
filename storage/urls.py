from django.urls import path
from rest_framework.routers import DefaultRouter

from storage.views import FolderViewSet, FileViewSet

router = DefaultRouter()
router.register(r'folders', FolderViewSet, basename='folders')
router.register(r'files', FileViewSet, basename='files')
urlpatterns = router.urls
