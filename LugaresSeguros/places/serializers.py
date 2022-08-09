from rest_framework import serializers
from places.models import Place #De places se trae Place

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'