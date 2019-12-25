from django.urls import path
from . import views

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<int:article_id>', views.article_detail, name='detail'),
]