from rest_framework import generics

from users.models import User
from users.serializers import ForAuthUserSerializers, ForCreateUserSerializers
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsUserProfile


class UsersListView(generics.ListAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class UsersDetailView(generics.RetrieveAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class UsersCreateView(generics.CreateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)

class UsersUpdateView(generics.UpdateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()
    permission_classes = [IsUserProfile]

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)