from rest_framework import generics, permissions

from users.models import CustomUser, Profile
from users.serializers import CustomUserSerializer, ProfileSerializer


class CustomUserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CustomUserSerializer

    def get_queryset(self):
        return CustomUser.objects.filter(pk=self.request.user.pk)


class ProfileList(generics.ListAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)


class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
