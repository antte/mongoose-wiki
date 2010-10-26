from article.models import *
from django.contrib import admin


admin.site.register(Article, ArticleAdmin)
admin.site.register(TranslationPattern, TranslationPatternAdmin)

