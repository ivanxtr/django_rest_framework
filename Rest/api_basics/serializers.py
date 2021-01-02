from rest_framework import serializers
from .models import Article

''' old way of doing it !!! 
class ArticleSerializer(serializers.Serializer):
  title = serializers.CharField(max_length=100)
  author = serializers.CharField(max_length=100)
  email = serializers.CharField(max_length=100)
  date = serializers.DateField()

  def create(self, validated_data):
    return Article.objects.create(validated_data)
  
  def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.author = validated_data.get('title', instance.author)
    instance.email = validated_data.get('title', instance.email)
    instance.date = validated_data.get('title', instance.date)
    instance.save()
    return instance
'''

class ArticleSerializer(serializers.ModelSerializer): 
  class Meta: 
    model = Article
    fields = ['id', 'title', 'author']
