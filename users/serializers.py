from rest_framework import serializers

from course.models import Paying
from users.models import User

class UserPayingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Paying
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    paying = UserPayingSerializers(source='paying_set', many=True, read_only=True,)

    def create(self, validated_data):
        paying = validated_data.pop('payment_set')
        user = User.objects.create(**validated_data)

        for pay in paying:
            Paying.objects.create(user=user, **pay)

        return user

    class Meta:
        model = User
        fields = ('id','name','email', 'phone', 'city','paying')


