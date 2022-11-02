from django.urls import path
from .views import encode, decode, stats
app_name = 'pasts'
urlpatterns = [
    path('encode', encode.as_view()),
    path('decode', decode.as_view()),
    path('stats', stats.as_view())
]
