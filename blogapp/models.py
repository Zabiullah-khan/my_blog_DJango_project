from django.db import models

# Create your models here.
class NewsFeed(models.Model):
	date = models.DateField(auto_now = True)
	title = models.CharField(max_length=50)
	postarea = models.TextField(max_length=5000)
	

