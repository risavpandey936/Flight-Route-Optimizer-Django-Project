from django.urls import path
from .views import home, bellman_ford

urlpatterns = [
    path('', home, name='home'),
    path('api/shortest-path/', bellman_ford, name='shortest_path_api'),
]




