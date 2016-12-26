from rest_framework import viewsets, permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from djangorest_example.models import Employee
from djangorest_example.serializers import EmployeeSerializer


class JwtEmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = [JSONWebTokenAuthentication]
