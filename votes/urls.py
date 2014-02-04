from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.core.urlresolvers import reverse_lazy

from votes import views

urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^candidate/(?P<pk>\d+)/$',
        views.CandidateView.as_view(),
        name='candidate'),

    url(r'^candidate/(?P<pk>\d+)/history$',
        views.candidate_history,
        name='candidate_history'),

    # used for voting in a form
    url(r'^votes/$', views.batch_vote, name='batch_vote'),

    # used for single vote
    url(r'^vote/$', views.vote, name='vote'),

    url(r'^accounts/register/$', views.register, name='register'),

    url(r'^accounts/login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'votes/login.html'}, name="login"),

    url(r'^accounts/logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': reverse_lazy('votes:index')}, name="logout"),

    url(r'^add-candidate/new/$', views.CreateCandidateView.as_view(), name='add-candidate'),
    url(r'^add-candidate/$', views.add_candidate_from_fb, name='add-from-fb'),

    url(r'^search/$', views.search, name='autocomplete-search'),

)
