from django.urls import path
from watchlistapp.views import HelloworldView

urlpatterns = [
  path("hello_world/",HelloworldView,name="hello_world" ),
]
