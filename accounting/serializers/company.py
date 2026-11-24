import re
from rest_framework import serializers
from accounting.models import Company

class CompanySerializer(serializers.ModelSerializer):
    company_type_display = serializers.CharField(
        source="get_company_type_display",
        read_only=True,
    )

    class Meta:
        model = Company
        fields = [
            "id",
            "name",
            "tax_code",
            "company_type",
            "company_type_display",
            "created_at",
            "updated_at",
        ]
        read_only_fields=["id","created_at","updated_at"]

    def validate_name(self, value):
        cleaned = value.strip()
        if not cleaned:
            raise serializers.ValidationError("Tên công ty không được để trống")
        return cleaned

    def validate_tax_code(self, value):
        cleaned = value.strip()
        if not re.match(r"^\d{10}(-\d{3})?$",cleaned):
            raise serializers.ValidationError("Mã số thuế phải gồm 10 chữ số hoặc 10 chữ số kèm '-xxx'")
        return cleaned