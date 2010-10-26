from django.template import loader, Context, RequestContext
from django.http import HttpResponse, HttpResponseRedirect
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
    
    c = RequestContext(request, {"article" : article})
    
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
		return HttpResponseRedirect("/article/view/"+articleTitle)
	else:	
		try:
			article = Article.objects.get(title = articleTitle)
			
		except Article.DoesNotExist:
			article = Article(title=articleTitle)
			form = ArticleForm(instance=article)
		else:
			form = ArticleForm(instance=article)
		c = RequestContext(request, {"articleTitle" : articleTitle, "form" : form})
		t = loader.get_template("edit.html")
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
    c = RequestContext(request, {"results" : results})
    
    return HttpResponse(t.render(c))
    

