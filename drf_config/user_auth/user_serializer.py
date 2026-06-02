from rest_framework import serializers

from .models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields ='__all__'
    def validate_email(self,value):
        data=UserModel.objects.filter(email=value)
        if data.exists():
            raise serializers.ValidationError("Email already exists")
        return value