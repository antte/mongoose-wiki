# Article application specific URL patterns (all URLs start with "/article")

from django.conf.urls.defaults import *
from mongoose_wiki.article.views import *

urlpatterns = patterns('',
    
    (r'^$', index),
    (r'^view/$', index),
    (r'^view/(?P<articleTitle>.+)/$', view),
	(r'^edit/(?P<articleTitle>.+)/$', edit),
	(r'^history/(?P<articleTitle>.+)/$', history),
    
)