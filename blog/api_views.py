# import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from blog.models import Post
from blog.api.serializers import PostSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# def post_to_dict(post):
# 	return {
# 		"pk": post.pk,
# 		"author_id": post.author_id,
# 		"created_at": post.created_at,
# 		"modified_at": post.modified_at,
# 		"published_at": post.published_at,
# 		"title": post.title,
# 		"slug": post.slug,
# 		"summary": post.summary,
# 		"content": post.content,
# 	}

# @csrf_exempt
@api_view(["GET", "POST"])
def post_list(request):
	if request.method == "GET":
			posts = Post.objects.all()
			return Response({"data": PostSerializer(posts, many=True).data})

	elif request.method == "POST":
			# post_data = json.loads(request.body)
			serializer = PostSerializer(data=request.data)
			if serializer.is_valid():
				post = serializer.save()
				return Response(PostSerializer(post).data, status=HTTPStatus.CREATED, headers={"Location": reverse("api_post_detail", args=(post.pk,))},)
	
			return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)

# @csrf_exempt
@api_view(["GET", "PUT", "DELETE"])
def post_detail(request, pk):
		try:
		    post = Post.objects.get(pk=pk)
    		# post = get_object_or_404(Post, pk=pk)
		except Post.DoesNotExist:
		    return Response(status=HTTPStatus.NOT_FOUND)

		if request.method == "GET":
				return Response(PostSerializer(post).data)
		elif request.method == "PUT":
				# post_data = json.loads(request.body)
				serializer = PostSerializer(post, data=request.data)
				if serializer.is_valid():
					serializer.save()
					return Response(status=HTTPStatus.BAD_REQUEST)

				return Response(serializer.errors, status=HTTPStatus.BAD_REQUEST)				        
		elif request.method == "DELETE":
				post.delete()
				return Response(status=HTTPStatus.NO_CONTENT)    


