from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from meme.models import Post
from meme.api.serializers import PostSerializer


# This API Functon is called for all POST requests and to GET all the memes
@api_view(['GET', 'POST'])
def api_post(request):

    if request.method == "GET":
        try:
            post = reversed(Post.objects.all()[:100])
        except Post.DoesNotExist:
            return Response({}, safe=False)
        serializer = PostSerializer(post, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            caption = serializer.validated_data["caption"]
            url = serializer.validated_data["url"]
            post = Post.objects.filter(
                name=name, caption=caption, url=url).count()
            if post > 0:
                return Response(status=status.HTTP_409_CONFLICT)

            serializer.save()
            post = Post.objects.get(name=name, caption=caption, url=url)
            d = {"id": post.id}
            return JsonResponse(d, status=status.HTTP_201_CREATED, safe=False)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This API Functon is called for all PATCH requests and to GET memes by id
@api_view(['GET', 'PATCH'])
def api_post_id(request, id):
    try:
        post = Post.objects.get(id=id)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PATCH":

        d = {
            "name": post.name,
            "caption": request.data['caption'],
            "url": request.data['url']}

        serializer = PostSerializer(data=d)
        if serializer.is_valid():
            name = serializer.data["name"]
            caption = serializer.data["caption"]
            url = serializer.data["url"]
            post2 = Post.objects.filter(
                name=name, caption=caption, url=url).count()
            if post2 > 0:
                return Response(status=status.HTTP_409_CONFLICT)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = request.data
        post.name = post.name
        post.caption = data.get("caption", post.caption)
        post.url = data.get("url", post.url)
        post.date_posted = data.get("date_posted", post.date_posted)
        post.save()

    serializer = PostSerializer(post)
    return JsonResponse(serializer.data)
