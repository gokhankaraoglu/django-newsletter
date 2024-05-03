from rest_framework import serializers
from news.models import Article, Journalist

from datetime import datetime
from datetime import date
from django.utils.timesince import timesince

class ArticleSerializer(serializers.ModelSerializer):
  time_since_pub = serializers.SerializerMethodField()
  # writer = serializers.StringRelatedField()
  # writer = JournalistSerializer()


  class Meta:
    model = Article
    fields = '__all__'
    # fields = ['title', 'description', 'text']
    # exclude = ['title', 'description', 'text']
    read_only_fields = ['id', 'created_at', 'updated_at']

  def get_time_since_pub(self, object):
    now = datetime.now()
    pub_date = object.published_at
    if object.isActive:
      time_delta = timesince(pub_date, now)
      return time_delta
    else:
      return "Not active!"
  
  def validate_published_date(self, date_value): #value level
    today = date.today()
    if date_value > today:
      raise serializers.ValidationError(f"Published date cannot be later than today")
    return date_value

class JournalistSerializer(serializers.ModelSerializer):

  # articles = ArticleSerializer(many=True, read_only=True)
  articles = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="article-detail")

  class Meta:
    model = Journalist
    fields = '__all__'
  

#### STANDARD SERIALIZER
# class ArticleSerializer(serializers.Serializer):
#   id = serializers.IntegerField(read_only=True)
#   writer = serializers.CharField()
#   title = serializers.CharField()
#   description = serializers.CharField()
#   text = serializers.CharField()
#   city = serializers.CharField()
#   published_date = serializers.DateField()
#   isActive = serializers.BooleanField()
#   created_at = serializers.DateTimeField(read_only=True)
#   updated_at = serializers.DateTimeField(read_only=True)

#   def create(self, validated_data):
#     print (validated_data)
#     return Article.objects.create(**validated_data)
#   def update(self, instance, validated_data):
#     instance.writer = validated_data.get("writer", instance.writer)
#     instance.title = validated_data.get("title", instance.title)
#     instance.description = validated_data.get("description", instance.description)
#     instance.text = validated_data.get("text", instance.text)
#     instance.city = validated_data.get("city", instance.city)
#     instance.published_date = validated_data.get("published_date", instance.published_date)
#     instance.isActive = validated_data.get("isActive", instance.isActive)
#     instance.save()
#     return instance
  
#   def validate(self, data): #object level
#     if data['title'] == data['description']:
#       raise serializers.ValidationError('Title and description will not be the same. Please enter different values')
#     return data
  
#   def validate_title(self, value): #value level
#     if len(value) < 20:
#       raise serializers.ValidationError(f"Title cannot be less than 20 characters. You entered {len(value)} characters")
#     return value