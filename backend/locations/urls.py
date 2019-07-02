from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'countries', views.CountryViewSet)
router.register(r'cities', views.CityViewSet)


urlpatterns = router.urls