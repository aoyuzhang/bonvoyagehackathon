from django.db import models
from django.contrib.auth.models import User


class Restaurent(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.CharField(max_length=100)

class Food(models.Model):
  name = models.CharField(max_length=30, unique=True)
  description = models.CharField(max_length=100)

class Post_for_food(models.Model):
  message = models.TextField(max_length=4000)
  restaurent = models.ForeignKey(Food, related_name='postsFood',on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True)
  created_by = models.ForeignKey(User, related_name='postsFood',on_delete=models.CASCADE)
  updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete =models.PROTECT)

class Post_for_restaurent(models.Model):
  message = models.TextField(max_length=4000)
  food = models.ForeignKey(Food, related_name='postsResto', on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(null=True)
  created_by = models.ForeignKey(User, related_name='postsResto',on_delete=models.CASCADE)
  updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete =models.PROTECT)