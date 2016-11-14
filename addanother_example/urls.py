from django.conf.urls import url

from addanother_example.views import CreateTeam, EditTeam

urlpatterns = [
    url(r'^team/add/$', CreateTeam.as_view(), name='addanother-add-team'),
	url(r'^team/edit/(?P<pk>.*)/$', EditTeam.as_view(), name='addanother-update-team'),
]