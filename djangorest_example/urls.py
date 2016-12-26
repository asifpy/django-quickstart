from django.conf.urls import url, include
from rest_framework import routers


from .views import EmployeeViewSet, CompanyViewSet

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'companies', CompanyViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^jwt/', include('djangorest_example.jwt_example.urls')),
]