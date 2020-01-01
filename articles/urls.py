from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_page'),
    path('article/<int:article_id>/', views.showArticle, name='show_article'),
    path('type/<str:art_type>/', views.showList, name='show_list'),
    path('author/<int:n_author>/', views.showAuthor, name='show_author'),
    path('tag/<int:n_tag>/', views.showTag, name='show_tag'),
    path('submission', views.submission, name='submission'),
    path('call_for_paper', views.callForPaper, name='call_for_paper'),
    path('about', views.about, name='about')
]

#author_name=Californian FB Text
