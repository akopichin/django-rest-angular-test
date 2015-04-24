# urls.py
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from annotations import views

urlpatterns = [
    url(r'^annotation/?$', views.annotation_list),
    url(r'^annotation/form$', views.annotation_form),
    url(r'^annotation/(?P<pk>[0-9]+)$', views.annotation_detail),
    url(r'^annotation/(?P<pk>[0-9]+)/prev/?$', views.annotation_prev),
    url(r'^annotation/(?P<pk>[0-9]+)/next/?$', views.annotation_next),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)
