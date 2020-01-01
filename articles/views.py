from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponse
from .models import Article, Author, Tag

# Create your views here.

def index(request):
    latest_article_list = Article.objects.order_by('-created_date')[:10]
    context = {'latest_article_list': latest_article_list}
    return render(request, 'articles/index.html', context)


def showArticle(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'articles/article.html',
                  {
                      'article': article,
                      'url': 'http://ducsulpr.du.ac.bd/article/'+str(article_id),
                   })


def showList(request, art_type):
    if(art_type == "journal"):
        art_list = Article.objects.filter(article_type='J').order_by('-created_date')
        return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : 'Journals'})
    elif(art_type == "blog"):
        art_list = Article.objects.filter(article_type='B').order_by('-created_date')
        return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : 'Blogs'})
    elif(art_type == "bookreview"):
        art_list = Article.objects.filter(article_type='R').order_by('-created_date')
        return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : 'Book Reviews'})
    elif(art_type == "DUThinks"):
        art_list = Article.objects.filter(article_type='L').order_by('-created_date')
        return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : 'DU Thinks'})

    elif(art_type == "LPRNews"):
        art_list = Article.objects.filter(article_type='N').order_by('-created_date')
        return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : 'LPR News'})
 

def showAuthor(request, n_author):
    i_author = get_object_or_404(Author, pk=n_author)
    art_list = i_author.article_set.all()
    return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : i_author.name})


def showTag(request, n_tag):
    i_tag = get_object_or_404(Tag, pk=n_tag)
    art_list = i_tag.article_set.all()
    return render(request, 'articles/content.html', {'art_list': art_list, 'art_type' : 'Tag : ' + i_tag.word})


def submission(request):
    return render_to_response('articles/submission.html')

def callForPaper(request):
    return render_to_response('articles/call_for_paper.html')



def about(request):
    return render_to_response('articles/about.html')
