
from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^$',  views.index, name="index"),
    #localhost/polls/

    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name="detail"),
    # localhost/polls/1

    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name="results"),
    # localhost/polls/1/results

   # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name="vote"),
    # localhost/polls/1/vote



]