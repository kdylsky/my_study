from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView

from music.serializers import MusicSerialzier
from music.models import Music

class MusicView(APIView):
    def get(self, request):
        obj = Music.objects.all()
        data = MusicSerialzier(instance=obj, many=True)
        return JsonResponse(data.data, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        data = request.data
        params = MusicSerialzier(data=data)
        params.is_valid(raise_exception=True)
        params.save()
        return JsonResponse(params.data, status=status.HTTP_200_OK)
