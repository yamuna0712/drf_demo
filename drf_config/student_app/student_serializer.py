from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
    def validate_name(self,value):
        data=Student.objects.filter(name=value)
        if data.exists():
            raise serializers.ValidationError("Name already exists")
        return value

    def validate_phone(self, value):
        if value.startswith("91"):
            return value
        raise serializers.ValidationError("Phone number is invalid")


