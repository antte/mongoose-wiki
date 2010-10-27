from django.db import models
from django.contrib import admin
from django.forms import ModelForm
from django.contrib.auth.models import User
import re

class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=2048)
    editors = models.ManyToManyField(User, through='UserEditsArticle')
    
    def __unicode__(self):
        return self.title
    
    # @return: a list of article titles
    def search(self, queryString):
        
        queryString = self.escapeHtmlEntities(queryString)
        
        results = []
        
        for article in self.__class__.objects.all():
            if re.search(queryString, article.title):
                results.append(article)
        
        for article in self.__class__.objects.all():
            alreadyInResults = False
            
            for result in results:
                if (result == article.title):
                    alreadyInResults = True
            
            if re.search(queryString, article.body) and not alreadyInResults:
                results.append(article)
        
        return results
    
    def getBodyToHTML(self):
        # We don't want to be destructive and change self.body
        body = self.body 
        
        # We escape before translating so that we don't destroy our new
        # HTML tags from the translation 
        body = self.escapeHtmlEntities(body)
        body = TranslationPattern().replaceAll(body)
        
        return body
    
    def escapeHtmlEntities(self, text):
        html_escape_table = {
            "&": "&amp;",
            '"': "&quot;",
            "'": "&apos;",
            ">": "&gt;",
            "<": "&lt;",
        }
        return "".join(html_escape_table.get(c,c) for c in text)
    
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']

class TranslationPattern(models.Model):
    needle = models.CharField(max_length=256)
    replace = models.CharField(max_length=256)
    def replaceAll(self, text):
        translationPatterns = self.__class__.objects.all()
        for translationPattern in translationPatterns:
            if translationPattern.needle == "\[\[(\w+)\]\]":
                for match in re.finditer(translationPattern.needle, text):
                    linkClass = ""
                    
                    try:
                        Article.objects.get(title=match.group(1))
                    except Article.DoesNotExist:
                        linkClass = "doesNotExist"
                    
                    replaceText  = '<a href="/article/view/'+match.group(1)+'"'
                    replaceText += 'class="'+linkClass+'">'+match.group(1)+'</a>'
                    
                    originalText = "\[\["+match.group(1)+"\]\]"
                    
                    text = re.sub(originalText, replaceText, text)
            else:
                text = re.sub(translationPattern.needle, translationPattern.replace, text)
        return text

class TranslationPatternAdmin(admin.ModelAdmin):
    list_display = ('needle', 'replace')

class ArticleForm(ModelForm):
    class Meta:
        exclude = ('editors',)
        model = Article

class UserEditsArticle(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    timestamp = models.DateTimeField(auto_now=True)
    change = models.TextField(max_length=2048)
    
    def getChange(self):
        return self.escapeHtmlEntities(self.change)
    
    # copy pasted (i know) from article model
    #@see: Article.escapeHtmlEntities()
    def escapeHtmlEntities(self, text):
        html_escape_table = {
            "&": "&amp;",
            '"': "&quot;",
            "'": "&apos;",
            ">": "&gt;",
            "<": "&lt;",
        }
        return "".join(html_escape_table.get(c,c) for c in text)

class UserEditsArticleAdmin(admin.ModelAdmin):
    list_display = ['user', 'article', 'timestamp']