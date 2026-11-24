from django.db.models import Q
from rest_framework import viewsets
from accounting.models import Company
from accounting.serializers import CompanySerializer

class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class=CompanySerializer

    def get_queryset(self):
        queryset = Company.objects.all()

        company_type= self.request.query_params.get("company_type")
        if company_type:
            queryset = queryset.filter(company_type=company_type.strip().upper())

        search = self.request.query_params.get("search")
        if search:
            keyword = search.strip()
            queryset = queryset.filter(Q(name__icontains=keyword)|Q(tax_code__icontains=keyword))

        return queryset