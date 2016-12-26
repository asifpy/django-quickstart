from rest_framework import viewsets

from .models import Company, Employee
from .serializers import EmployeeSerializer, CompanySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # def get_queryset(self):
    #     return Employee.objects.none()


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
