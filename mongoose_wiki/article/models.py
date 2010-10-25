from django.db import models
from django.contrib import admin
import re
from django.forms import ModelForm


class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=2048)
    
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
            text = re.sub(translationPattern.needle, translationPattern.replace, text)
        return text
    
class TranslationPatternAdmin(admin.ModelAdmin):
    list_display = ('needle', 'replace')
	
class ArticleForm(ModelForm):
	class Meta:
		model = Article
	