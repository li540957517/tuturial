from django.conf.urls import url
from . import views

app_name = 'learn'
urlpatterns = [
    url(r'^$', view=views.home, name='home'),
    url(r'^rsp/$', view=views.rsp_attr, name='rsp_attr'),
    url(r'^rsp/redirect/$', view=views.rsp_redirect, name='rsp_redirect'),
    url(r'^rsp/json/$', view=views.rsp_json, name='rsp_json'),
    url(r'^rsp/header/$', view=views.rsp_header, name='rsp_header'),
    url(r'^rsp/download/$', view=views.rsp_download, name='rsp_download'),
    url(r'^tmp/loading/$', view=views.tmp_loading, name='tmp_loading'),
    url(r'^tmp/render/$', view=views.tem_render, name='tmp_render'),
    url(r'^tmp/article/$', view=views.tmp_article, name='tmp_article'),
    url(r'^dtl/syntax/$', view=views.dtl_syntax, name='dtl_syntax'),
    url(r'^dtl/tags/$', view=views.dtl_tags, name='dtl_tags'),
    url(r'^dtl/filter/$', view=views.dtl_filter, name='dtl_filter'),
    url(r'^dtl/tmp/$', view=views.dtl_tmp_inheritance, name='dtl_tmp_inheritance'),
    url(r'^dtl/tmp2/$', view=views.dtl_tmp_inheritance2, name='dtl_tmp_inheritance2'),
]
