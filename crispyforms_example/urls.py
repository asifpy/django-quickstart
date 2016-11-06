from django.conf.urls import url

from crispyforms_example.views import crispy_view

urlpatterns = [
    url(r'^$', crispy_view, name='crispy-view'),
]