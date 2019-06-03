from django.conf.urls import url
from django.urls import path, include

from django.conf import settings
from django.contrib import admin
admin.autodiscover()

import hello.views
from rest_framework.documentation import include_docs_urls

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('greetings/', include('greetings.urls')),
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]

if (settings.DEBUG):
    from rest_framework_swagger.views import get_swagger_view
    
    schema_view = get_swagger_view(title='Pastebin API')

    urlpatterns += [
        url(r'^docs/', include_docs_urls(title='Sample API')),
        url(r'^swagger/$', schema_view)
    ]