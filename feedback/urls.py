from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [
    url(r'^$', view=views.home, name='feedback'),
    url(r'^postdata/$', view=views.get_feedback_data, name='get_feedback_data'),
    url(r'^form/$', view=views.feedback_form, name='feedback_form'),
    url(r'^list/$', view=views.feedback_list, name='feedback_list'),
    url(r'^(?P<fid>\d{1,4})/$', view=views.feedback_detail, name='feedback_detail'),
    url(r'^edit/(?P<fid>\d{1,4})/$', view=views.feedback_edit, name='feedback_edit'),
    url(r'^del/(?P<fid>\d{1,4})/$', view=views.feedback_delete, name='feedback_delete'),
    url(r'^login/$', view=views.login, name='login'),
    url(r'^logout/$', view=views.logout, name='logout'),
]
