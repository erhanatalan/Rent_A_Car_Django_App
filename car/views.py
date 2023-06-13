from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Car, CarSerializer,
    Reservation, ReservationSerializer,
)


# FixView
class FixView(ModelViewSet):
    pass


# CarView
from .permissions import IsStaffOrReadOnly
class CarView(FixView):
    queryset = Car.objects.filter(availabilty=True)
    serializer_class = CarSerializer
    permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):

        if self.request.user.is_staff:
            queryset = Car.objects.all()
        else:
            queryset = super().get_queryset()

        return queryset
    


# ReservationView
class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    