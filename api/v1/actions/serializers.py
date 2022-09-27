from rest_framework.serializers import ModelSerializer
from web.models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = ("__all__")