# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('',views.index),
#     path('', views.get_current_weather, name='get_current_weather'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_current_weather/', views.get_current_weather, name='get_current_weather'),
]