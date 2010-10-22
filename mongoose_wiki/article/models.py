from django.db import models
import re

class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=2048)
    
    def getBodyToHTML(self):
        # We don't want to be destructive and change self.body
        body = self.body 
        
        # We escape before translating so that we don't destroy our new
        # HTML tags from the translation 
        body = self.escapeHtmlEntities(body)
        
        body = self.replaceAllTranslationPatterns(body)
        
        return body
    
    def replaceAllTranslationPatterns(self, body):
        translationPatterns = TranslationPattern.objects.all()
        for translationPattern in translationPatterns:
            body = re.sub(translationPattern.needle, translationPattern.replace, body)
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

class TranslationPattern(models.Model):
    needle = models.CharField(max_length=256)
    replace = models.CharField(max_length=256)