from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from app_f import views


urlpatterns = [
    path('', views.index, name='index'),
    # REST
    path('user/', views.UserList.as_view(), name='user-list'),
    path('user/crear/', views.UserCreate.as_view(), name='user-crear'),
    path('user/<int:pk>', views.UserDetail.as_view(), name='user-detalle'),


    path('producto/', views.ProductoList.as_view(), name='producto-list'),
    path('producto/crear/', views.ProductoCreate.as_view(), name='producto-crear'),
    path('producto/<int:pk>/', views.ProductoDetail.as_view(),
         name='producto-detalle'),

]
urlpatterns = format_suffix_patterns(urlpatterns)
