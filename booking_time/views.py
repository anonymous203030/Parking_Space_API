from django.db import IntegrityError
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import BookTime, ReserveBookTime
from .permissions import IsManager, IsOwner
from .serializers import BookTimeSerializer, ReserveSerializer


# Book Time

class CreateBookTimeAPIViewSet(CreateAPIView):
    queryset = BookTime.objects.all()
    serializer_class = BookTimeSerializer
    permission_classes = [IsManager | IsAdminUser]


class BookTimeDetailsAPIViewSet(RetrieveUpdateDestroyAPIView):
    queryset = BookTime.objects.all()
    serializer_class = BookTimeSerializer
    permission_classes = [IsManager | IsAdminUser]


class BookTimeListAPIViewSet(ListAPIView):
    queryset = BookTime.objects.all()
    serializer_class = BookTimeSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['floor', 'parking_space_id', 'owner__username', 'owner_email']
    filterset_fields = ['booking_start_time', 'booking_end_time']


# Reserve Book Time
class CreateReserveAPIVIewSet(CreateAPIView):
    queryset = ReserveBookTime.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated | IsAdminUser]

    # I didn't added IsEmployee permission because i thought that maybe
    # manager could reserve parking space too, overwise i would just create new permissions like IsManager and add into
    # permission_classes
    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise ValidationError({"400 Bad Request": "Owner field must be unique."})


class ListReserveAPIViewSet(ListAPIView):
    queryset = ReserveBookTime.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['book_time__floor', 'book_time__parking_space_id', 'owner__username', 'owner__email']
    filterset_fields = ['created_at', 'updated_at']
    ordering_fields = ['created_at', 'updated_at']


class DetailsReserveAPIViewSet(RetrieveUpdateDestroyAPIView):
    queryset = ReserveBookTime.objects.all()
    serializer_class = ReserveSerializer
    permission_classes = [IsOwner | IsAdminUser]
