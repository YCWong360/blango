from django.urls import path, include
from rest_framework.authtoken import views
from blog.api.views import PostList, PostDetail

urlpatterns = [
	path("api/v1/posts/", PostList.as_view(), name="api_post_list"),
	path("api/v1/posts/<int:pk>", PostDetail.as_view(), name="api_post_detail"),
	path("auth/", include("rest_framework.urls")),
	path("token-auth/", views.obtain_auth_token)
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),		
]