from rest_framework import serializers
from .models import Hudud, QurilishTashkiloti, QurilishBino



class HududSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hudud
        fields = ['name', 'author']


class QurilishTashkilotiSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishTashkiloti
        fields = '__all__'


class QurilishBinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = QurilishBino
        fields = '__all__'