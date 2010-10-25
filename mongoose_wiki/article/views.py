from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
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
			
		except Article.DoesNotExist: #TODO 404?
			t = loader.get_template("edit.html")
			c = Context({"articleTitle" : articleTitle})
		form = ArticleForm(instance=article)
		t = loader.get_template("edit.html")
		c = Context({"articleTitle" : articleTitle, "form" : form})
	
	return HttpResponse(t.render(c))