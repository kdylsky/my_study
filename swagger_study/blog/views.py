from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from blog.serializers import BlogSerializer
from drf_yasg.utils import swagger_auto_schema, no_body


class BlogView(APIView):
    @swagger_auto_schema(    
        request_body=no_body,
        query_serializer=BlogSerializer,
        responses={200 : BlogSerializer}
    )
    def get(self, reqeust):
        return JsonResponse({"resutl":"ok"}, status=status.HTTP_200_OK )
    
    @swagger_auto_schema(
        request_body=BlogSerializer,
        responses={200 : "Success"}
    )
    def post(self, request):
        return JsonResponse({"resutl":"ok"}, status=status.HTTP_200_OK )