from django.urls import path, include
from rest_framework.authtoken import views
from blog.api_views import post_list, post_detail

urlpatterns = [
	path("api/v1/posts/", post_list, name="api_post_list"),
	path("api/v1/posts/<int:pk>", post_detail, name="api_post_detail"),
	path("auth/", include("rest_framework.urls")),
	path("token-auth/", views.obtain_auth_token)
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),		
]