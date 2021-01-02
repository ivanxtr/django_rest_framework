# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer

# Create your views here.

# ViewSets
class ArticleViewSet(viewsets.ViewSet):
  def list(self, request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

  def create(self, request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def retrieve(self, request, pk=None):
    queryset = Article.objects.all()
    article = get_object_or_404(queryset, pk=pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  
  def update(self, request, pk=None):
    article = Article.objects.get(pk=pk)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# generic api
class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
  serializer_class = ArticleSerializer
  queryset = Article.objects.all()
  lookup_field = 'id'
  # Session Auth
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request, id =None):
    if id:
      return self.retrieve(request)
    return self.list(request)

  def post(self, request):
    return self.create(request)

  def put(self, request, id):
    return self.update(request, id)
  
  def delete(self, request, id):
    return self.destroy(request, id)

# class api view
class ArticleAPIView(APIView):
  # Token Auth
  # example Token [token_number]
  authentication_classes = [TokenAuthentication]
  permission_classes = [IsAuthenticated]

  def get(self, request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ArticleDetails(APIView):
  def get_object(self, id):
    try:
      return Article.objects.get(id=id)
    except Article.DoesNotExist:
      return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    
  def get(self, request, id):
    article = self.get_object(id)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

  def put(self, request, id):
    article = self.get_object(id)
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, id):
    article = self.get_object(id)
    article.delete()
    return HttpResponse(status=status.HTTP_204_NO_CONTENT)

# functional api views
@api_view(['GET', 'POST'])
def article_list(request):
  if request.method == 'GET':
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def article_detail(request, pk):
  try:
    article = Article.objects.get(pk=pk)
  except Article.DoesNotExist:
    return HttpResponse(status=404)

  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

  if request.method == 'PUT':
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  if request.method == 'DELETE':
    article.delete()
    return HttpResponse(status=204)
