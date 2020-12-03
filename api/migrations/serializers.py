from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()