from rest_framework import serializers

from django.contrib.auth.models import AbstractUser
from app_f.models import *


class User_Ser(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['username', 'password', 'first_name',
                  'last_name', 'email', 'celular', 'direccion', 'ciudad']


class Producto_Ser(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ['id', 'producto_nombre', 'producto_marca', 'producto_modelo',
                  'producto_precio', 'producto_calificacion', 'producto_fecha_creacion']
