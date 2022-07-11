from django.urls import path, include

from blog.api_views import post_list, post_detail

urlpatterns = [
	path("posts/", post_list, name="api_post_list"),
	path("posts/<int:pk>", post_detail, name="api_post_detail"),
]

urlpatterns += [
    path("auth/", include("rest_framework.urls")),		
]