from article.models import *
from us_er.models import *
from django.contrib import admin


admin.site.register(Article, ArticleAdmin)
admin.site.register(TranslationPattern, TranslationPatternAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserEditsArticle, UserEditsArticleAdmin)
