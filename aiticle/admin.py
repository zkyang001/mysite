from django.contrib import admin
from .models import Article
# Registsser yodur models here.
# ×¢½â
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
	"""comment"""
	list_display = ('pk', 'title', 'content', 'author', 'is_delete', 'char_count', 'update_time',)
	ordering = ('id',)
	
# admin.site.register(Article, ArticleAdmin)
