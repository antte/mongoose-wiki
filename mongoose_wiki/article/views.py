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

def searchResults(request):
    
    query = ""
    
    if request.POST['q'] is not None:
        query = request.POST['q']
    
    article = Article()
    
    results = article.search(query)
    
    #Tests if results is an iterable object
    if not getattr(results, '__iter__', False):
        results = []
    
    t = loader.get_template("searchResults.html")
    c = Context({"results" : results})
    
    return HttpResponse(t.render(c))
    