from django.conf.urls import url
from . import views

app_name = 'feedback'

urlpatterns = [
    url(r'^$', view=views.home, name='feedback'),
    url(r'^postdata/$', view=views.get_feedback_data, name='get_feedback_data'),
    url(r'^form/$', view=views.feedback_form, name='feedback_form'),
]
