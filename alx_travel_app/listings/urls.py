from rest_framework.routers import DefaultRouter
from .views import ListingViewSet, BookingViewSet

router = DefaultRouter()
router.register(r"listings", ListingViewSet)
router.register(r"booking", BookingViewSet)

urlpatterns = router.urls
