from django.contrib import admin
from django.urls import path, include, re_path 
from rest_framework.permissions import AllowAny
from rest_framework import permissions
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi

"""
swagger에 등록할 urls을 입력
아래의 코드는 따로 등록 하는 코드없이 모든 것을 연결하지만
이와 같이 관리하면, 보여주고 싶은 부분만 swagger로 나타낼 수 있다.
"""
# schema_url_patterns = [ 
#     path('', include('blog.urls')),
#     path('', include('photo.urls')),
#     ]

# schema_view_v1 = get_schema_view(
#     openapi.Info(
#         title="Open API",
#         default_version='v1',
#         description="시스템 API",
#         terms_of_service="https://www.google.com/policies/terms/",
#     ),
#     public=True,
#     permission_classes=(AllowAny,),
#     patterns=schema_url_patterns,
# )

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',include('blog.urls')),
#     path('',include('photo.urls')),
#     re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view_v1.without_ui(cache_timeout=0), name='schema-json'),
#     re_path(r'^swagger/$', schema_view_v1.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     re_path(r'^redoc/$', schema_view_v1.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
# ]


schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # 관리자 url
    path("admin/", admin.site.urls),

    # 실제 앱 관련 url
    path("", include("blog.urls")),
    path("", include("photo.urls")),
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
