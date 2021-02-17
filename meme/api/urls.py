from django.urls import path
from meme.api.views import api_post, api_post_id


urlpatterns = [
    path('', api_post, name="meme-api"),
    path('<id>', api_post_id, name="meme-api-id")
]
