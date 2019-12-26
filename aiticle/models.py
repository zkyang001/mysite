from django.db import models
from django.contrib.auth.models import User

# Create your mod12els here.
class Article(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	create_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
	is_delete = models.BooleanField(default=False)
	char_count = models.IntegerField(default=10000)
	

	def __str__(self):
		return "<Article:%s>" % self.title