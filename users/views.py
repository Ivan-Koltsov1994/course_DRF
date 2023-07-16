from rest_framework import  generics

from users.models import User
from users.serializers import ForAuthUserSerializers, ForCreateUserSerializers


class UsersListView(generics.ListAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()

class UsersDetailView(generics.RetrieveAPIView):
    serializer_class = ForAuthUserSerializers
    queryset = User.objects.all()

class UsersCreateView(generics.CreateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)

class UsersUpdateView(generics.UpdateAPIView):
    serializer_class = ForCreateUserSerializers
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        return User.objects.filter(pk=user.id)