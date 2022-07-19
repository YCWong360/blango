from django.urls import path, include, re_path
from rest_framework.authtoken import views
from blog.api.views import PostViewSet, UserDetail, TagViewSet
from rest_framework.routers import DefaultRouter
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
import os

urlpatterns = [
	# path("api/v1/posts/", PostList.as_view(), name="api_post_list"),
	# path("api/v1/posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),    
	path("api/v1/users/<str:email>", UserDetail.as_view(), name="api_user_detail"),
]

router = DefaultRouter()
router.register("api/v1/tags", TagViewSet)
router.register("posts", PostViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Blango API",
        default_version="v1",
        description="API for Blango Blog",
    ),
    url=f"https://{os.environ.get('CODIO_HOSTNAME')}-8000.codio.io/api/v1/",
    public=True,
)

urlpatterns += [
    path("auth/", include("rest_framework.urls")),		
		path("token-auth/", views.obtain_auth_token),
		re_path(
        r"^api/v1/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "api/v1/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("", include(router.urls)),

]

