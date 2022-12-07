from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView

from music.serializers import MusicSerialzier
from music.models import Music

class MusicView(APIView):
    def get(self, request):
        obj = Music.objects.all()
        data = MusicSerialzier(instance=obj, many=True)
        f = open('./sentence/test.txt', 'r')
        sentence = f.readlines()
        f.close()
        return JsonResponse({"sentence":sentence, "data":data.data}, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        data = request.data
        params = MusicSerialzier(data=data)
        params.is_valid(raise_exception=True)
        params.save()
        f = open('./sentence/test.txt', 'a')
        f.write(request.data.get("title") + " what and asdasd ?????? " +request.data.get("author"))
        f.close()
        return JsonResponse(params.data, status=status.HTTP_200_OK)
