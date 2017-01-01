from django.conf.urls import url

from .views import githubrepos


urlpatterns = [
    url(r'^github/repos/', githubrepos, name='social-github-repos'),
]