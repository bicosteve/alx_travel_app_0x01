from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from drf_yasg.utils import swagger_auto_schema


from .models import Listing, Booking, Payment
from .serializers import ListingSerializer, BookingSerializer, PaymentSerializer


# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """This is viewset for managing payments"""

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_query(self):
        if getattr(self, "wagger_fake_view", False):
            return Payment.objects.none()

        user = self.request.user
        if user.is_staff:
            return Payment.objects.all()
        return Payment.objects.filter(booking_user=user)

    @swagger_auto_schema()
    @action(detail=True, methods=["GET"])
    def verify(self, request, pk=None):
        pass

    @action(detail=True, methods=["POST"])
    def initialize(self, request, pk=None):
        pass

    @swagger_auto_schema()
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
