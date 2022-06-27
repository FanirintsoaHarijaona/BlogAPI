from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
   permission_class           =  (IsAuthorOrReadOnly,)
   queryset                   =  Post.objects.all()
   serializer_class           =  PostSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset                   =  get_user_model().objects.all()
   serializer_class           =  UserSerializer
