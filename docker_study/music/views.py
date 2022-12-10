from django.http import JsonResponse

from rest_framework import status
from rest_framework.views import APIView

from music.serializers import MusicSerialzier
from music.models import Music

# class MusicView(APIView):
#     def get(self, request):
#         obj = Music.objects.all()
#         data = MusicSerialzier(instance=obj, many=True)
#         f = open('./sentence/test.txt', 'r')
#         sentence = f.readlines()
#         f.close()
#         return JsonResponse({"sentence":"ok", "data":data.data}, status=status.HTTP_200_OK, safe=False)

#     def post(self, request):
#         data = request.data
#         params = MusicSerialzier(data=data)
#         params.is_valid(raise_exception=True)
#         params.save()
#         f = open('./sentence/test.txt', 'a')
#         f.write(request.data.get("title") + " what and asdasd ?????? " +request.data.get("author"))
#         f.close()
#         return JsonResponse(params.data, status=status.HTTP_200_OK)


# host : "host.docker.internal" 내부로컬
# host : "DB컨테이너 ip주소"
# host : mysql-container   네트워크 구성된 컨테이너이름
class MusicView(APIView):
    def get(self, request):
        obj = Music.objects.all()
        data = MusicSerialzier(instance=obj, many=True)
        return JsonResponse({"sentence":"bad", "data":data.data}, status=status.HTTP_200_OK, safe=False)

    def post(self, request):
        data = request.data
        params = MusicSerialzier(data=data)
        params.is_valid(raise_exception=True)
        params.save()
        return JsonResponse(params.data, status=status.HTTP_200_OK)


