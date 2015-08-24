from django.shortcuts import render
from blog.models import Article
# from django.http import Http404
# from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    list = Article.objects.all()
    if len(list) > 5:
        list = list[:5]

    for l in list:
        sp = str(l.date).split('-')
        l.year = sp[0]
        l.month = '%s-%s' % (sp[1], sp[2])

    return render(request, 'index.html', {'list': list})


def detail(request, id):
    # try:
        article = Article.objects.get(id=id)
        dates = str(article.date).split('-')
        article.year = dates[0]
        article.month = '%s-%s' % (dates[1], dates[2])
        return render(request, 'detail.html', {'article': article})
    # finally:
    #     return Http404



def category(request):
    return render(request, 'category.html')


def tag(request):
    return render(request, 'tag.html')


def archive(request):
    return render(request, 'tag.html')


def reading(request):
    return render(request, 'tag.html')

def about(request):
    return render(request, 'tag.html')
