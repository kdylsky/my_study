from rest_framework import serializers
from music.models import Music

class MusicSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"
        