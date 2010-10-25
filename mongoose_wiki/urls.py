# Main URLs file, delegates responsibility to individual applications.

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mongoose_wiki import article
from mongoose_wiki.article.views import index as articleindex
from mongoose_wiki.article.views import searchResults as articlesearchresults

urlpatterns = patterns('',
    
    (r'^article/', include('mongoose_wiki.article.urls')),
    (r'^$', articleindex),
    
    (r'^search', articlesearchresults),
    
    # Example:
    # (r'^mongoose/', include('mongoose.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^admin/', include(admin.site.urls)),
    
)
