from django.urls import include, path
from rest_framework.routers import DefaultRouter
from accounting.views import CompanyViewSet

router = DefaultRouter()
router.register(f"companies",CompanyViewSet,basename="company")

urlpatterns=[
    path("",include(router.urls))
]