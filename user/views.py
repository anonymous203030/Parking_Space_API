from django.contrib.auth import get_user_model
from django.db import IntegrityError
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, GenericAPIView
from .models import UserProfile
from .permissions import IsProfileOwner
from .serializers import ProfileSerializer, RegisterSerializer, LoginSerializer


# Register User
class RegisterAPIViewSet(CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


# Login User

class LoginAPIViewSet(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        queryset = LoginSerializer.objects.filter(user=self.request.user)
        if queryset.exists():
            raise ValidationError('You have already signed up')
        serializer.save()


#  User Profile

class UserProfileCreate(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner | IsAdminUser]

    def perform_create(self, serializer):
        try:
            serializer.save(owner=self.request.user)
        except IntegrityError:
            raise ValidationError({"400 Bad Request": "Owner field must be unique."})


class UserProfileUpdate(RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner | IsAdminUser]


class UserProfileList(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
    search_fields = ['first_name', 'last_name', 'about', 'owner__username', 'owner__email']
    filterset_fields = ['gender', 'owner__profession']
    ordering_fields = ['created_at']
