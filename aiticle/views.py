from django.shortcuts import render_to_response, get_object_or_404
from .models import Article
# Create your views here.

def article_detail(request, article_id):
	blog = get_object_or_404(Article, pk=article_id)
	param = {}
	param['obj'] = blog
	return render_to_response('article_web.html', param)

def article_list(request):
	blogs = Article.objects.all()
	param = {}
	param['objs'] = blogs
	return render_to_response('article_list.html', param)