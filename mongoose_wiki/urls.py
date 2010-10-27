# Main URLs file, delegates responsibility to individual applications.

from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mongoose_wiki import article
from mongoose_wiki.article.views import index as articleindex
from mongoose_wiki.article.views import searchResults as articlesearchresults

#added for register and login
import os
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from articles.views import *

site_media = os.path.join(
  os.path.dirname(__file__), 'site_media'
)

urlpatterns = patterns('',
    
    (r'^article/', include('mongoose_wiki.article.urls')),
    (r'^$', articleindex),
    
    (r'^search', articlesearchresults),
    
    # Example:
    # (r'^mongoose/', include('mongoose.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    #(r'^admin/', include(admin.site.urls)),

    #added for register and login
    #(r'^$', main_page),
    (r'^user/(\w+)/$', user_page),
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),
    (r'^register/$', register_page),
    (r'register/success/$', direct_to_template,
    	{'template': 'registration/register_success.html'}),
    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root': site_media}),
    
)
