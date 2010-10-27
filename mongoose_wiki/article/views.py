from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from article.models import *


def index(request):
    return view(request, "start")

def view(request, articleTitle):
    
    try:
        article = Article.objects.get(title = articleTitle)
    except Article.DoesNotExist:
        t = loader.get_template("articleDoesNotExist.html")
        c = Context({"articleTitle" : articleTitle})
        return HttpResponse(t.render(c))
    
    t = loader.get_template("view.html")
    c = RequestContext(request, {"article" : article, "articleTitle" : article.title})
    
    return HttpResponse(t.render(c))

	
def edit(request, articleTitle):
    if request.method == 'POST':
        try:
            article = Article.objects.get(title = request.POST['title'])
        except Article.DoesNotExist:
            form = ArticleForm(request.POST)
        else:
            form = ArticleForm(request.POST, instance=article)
        new_article = form.save()
        editor = User.objects.get(username="antte")
        UserEditsArticle(article=new_article, user=editor).save()
        return HttpResponseRedirect("/article/view/"+articleTitle)
    else:
        try:
			article = Article.objects.get(title = articleTitle)
        except Article.DoesNotExist:
            article = Article(title=articleTitle)
        form = ArticleForm(instance=article)
        c = RequestContext(request, {"articleTitle" : articleTitle, "form" : form})
        t = loader.get_template("edit.html")
	return HttpResponse(t.render(c))

def history(request, articleTitle):
    try:
        article = Article.objects.get(title = articleTitle)
    except Article.DoesNotExist:
        t = loader.get_template("articleDoesNotExist.html")
        c = Context({"articleTitle" : articleTitle})
        return HttpResponse(t.render(c))
    
    try:
        edits = UserEditsArticle.objects.filter(article=article)
    except:
        edits = []
    
    c = Context({"edits" : edits, "articleTitle" : articleTitle, "article" : article})
    t = loader.get_template("history.html")
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
    c = RequestContext(request, {"results" : results, "searchQuery" : query})
    
    return HttpResponse(t.render(c))
    

