from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('annotations.urls')),
    url(r'^$', 'testprj.views.home', name='home'),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
]
