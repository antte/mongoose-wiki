from django.template import loader, Context
from django.http import HttpResponse
from article.models import *

def index(request):
    return view(request, "start")

def view(request, articleTitle):
    try:
        article = Article.objects.get(title = articleTitle)
    except Article.DoesNotExist: #TODO 404?
        raise Article.DoesNotExist
    
    t = loader.get_template("view.html")
    c = Context({"article" : article})
    
    return HttpResponse(t.render(c))