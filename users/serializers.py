from rest_framework import serializers

from course.models import Paying
from users.models import User

class UserPayingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paying
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    paying = UserPayingSerializers(source='paying_set', many=True, read_only=True,)

    class Meta:
        model = User
        fields = ('email', 'phone', 'city','paying')


