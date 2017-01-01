import requests
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class GitHubRepoView(LoginRequiredMixin, TemplateView):
    template_name = "repos.html"
    title = "My Github Repos"

    def repos(self):
        social = self.request.user.social_auth.get(provider='github')
        token = 'token {}'.format(social.extra_data['access_token'])
        username = self.request.user.username
        GITHUB_URI = 'https://api.github.com/users/{}/repos'.format(username)
        response = requests.get(GITHUB_URI, headers={'Authorization': token})
        return response.json()


githubrepos = GitHubRepoView.as_view()
