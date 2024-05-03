from django.db import models

# Create your models here.

class Journalist(models.Model):
  name= models.CharField(max_length=120)
  surname= models.CharField(max_length=120)
  biography= models.TextField(blank=True, null=True)

  def __str__(self):
    return f'{self.name} {self.surname}'

class Article(models.Model):
  writer = models.ForeignKey(Journalist, on_delete=models.CASCADE, related_name='articles')
  title = models.CharField(max_length=120)
  description = models.CharField(max_length=200)
  text = models.TextField()
  city = models.CharField(max_length=120)
  published_at = models.DateField()
  isActive = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title
