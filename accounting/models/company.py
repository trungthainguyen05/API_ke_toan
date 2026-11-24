from django.db import models

class Company(models.Model):
    class CompanyType(models.TextChoices):
        CUSTOMER = "CUSTOMER","Khách hàng"
        SUPPLIER = "SUPPLIER", "Nhà cung cấp"
        BOTH = "BOTH", "Cả hai"
        OTHER = "OTHER" , "Khác"

    name = models.CharField(max_length=255, verbose_name="Tên công ty")
    tax_code = models.CharField(
        max_length=20,
        unique=True,
        verbose_name="Mã số thuế",
    )
    company_type=models.CharField(
        max_length=20,
        choices=CompanyType.choices,
        default=CompanyType.CUSTOMER,
        verbose_name="Loại công ty",
    )
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        db_table="accounting_companies"
        ordering=["-created_at"]
        verbose_name = "Công ty"
        verbose_name_plural = "Danh sách công ty"

    def __str__(self):
        return f"{self.tax_code} - {self.name}"