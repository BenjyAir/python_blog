from django.shortcuts import render
from blog.models import Article


# from django.http import Http404
# from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    list = Article.objects.all()
    if len(list) > 5:
        list = list[:5]

    return render(request, 'index.html', {'list': list})


def detail(request, id):
    # try:
    article = Article.objects.get(id=id)
    return render(request, 'detail.html', {'article': article})
    # finally:
    #     return Http404


def category(request):
    list = Article.objects.all()
    m = {}
    for l in list:
        ca = l.category
        if ca in m.keys():
            m[ca].append(l)
        else:
            m[ca] = [l, ]
    counts = []
    for l in m:
        counts.append(len(l))
    return render(request, 'category.html', {'map': m, 'counts': counts})


def tag(request):
    list = Article.objects.all()
    m = {}
    for l in list:
        ca = l.tag
        if ca in m.keys():
            m[ca].append(l)
        else:
            m[ca] = [l, ]

    return render(request, 'tag.html', {'map': m})


def archive(request):
    list = Article.objects.all()
    cacheStr = ''
    ls = []
    m = {}
    for i, l in enumerate(list):
        sp = str(l.date).split("-")
        if i == 0:
            cacheStr = sp[0]
            ls.append(l)
        else:
            if cacheStr == sp[0]:
                ls.append(l)
            else:
                m[cacheStr] = ls
                ls = []
                ls.append(l)
                cacheStr = sp[0]

    if i == (len(list) - 1) and len(ls) != 0:
        m[cacheStr] = ls
        ls = []

    print(m.keys())
    return render(request, 'archive.html', {'map': m})


def reading(request):
    return render(request, 'tag.html')


def about(request):
    return render(request, 'tag.html')
