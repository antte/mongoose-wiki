from django.db import models
import re

class Article(models.Model):
    title = models.CharField(max_length=128)
    body = models.TextField(max_length=2048)
    
    def getBodyToHTML(self):
        translationPatterns = TranslationPattern.objects.all()
        print(translationPatterns)
        body = self.body
        for translationPattern in translationPatterns:
            #sub as in substitute? it replaces all instances of needle with replace
            body = re.sub(translationPattern.needle, translationPattern.replace, body)
        return body
    
class TranslationPattern(models.Model):
    needle = models.CharField(max_length=256)
    replace = models.CharField(max_length=256)