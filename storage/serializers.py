from rest_framework import serializers

from storage.models import TheFolder, TheFile


class TheFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheFile
        fields = '__all__'


class TheFolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheFolder
        fields = '__all__'


class TheFolderTreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TheFolder
        fields = ['folder_name', 'sub_folders']

    def get_fields(self):
        fields = super(TheFolderTreeSerializer, self).get_fields()
        fields['sub_folders'] = TheFolderTreeSerializer(many=True)
        return fields
