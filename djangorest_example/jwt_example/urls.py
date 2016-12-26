from django.conf.urls import url, include

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from djangorest_example.jwt_example.views import JwtEmployeeViewSet


router = routers.DefaultRouter()
router.register(r'employees', JwtEmployeeViewSet, base_name='jwt-employees')


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^obtain_token/', obtain_jwt_token),
]
