from django.db import models

# Create your mod1els here.
class Article(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()