from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from storage.models import TheFolder, TheFile
from storage.serializers import TheFolderSerializer, TheFolderTreeSerializer, TheFileSerializer


class FolderViewSet(ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """
    serializer_class = TheFolderSerializer
    queryset = TheFolder.objects.all()

    @action(detail=False, methods=['get'])
    def sub_folders(self, request):
        folders = TheFolder.objects.filter(parent_folder__isnull=True)
        serializer1 = TheFolderTreeSerializer(folders, many=True)
        return Response(serializer1.data, status=status.HTTP_200_OK)


class FileViewSet(ModelViewSet):
    """
    A viewset for viewing and editing folder instances.
    """
    serializer_class = TheFileSerializer
    queryset = TheFile.objects.all()
