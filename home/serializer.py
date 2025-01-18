from rest_framework import serializers

class PersonSerilizer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()
