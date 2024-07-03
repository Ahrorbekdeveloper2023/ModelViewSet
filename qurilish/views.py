from django.shortcuts import render
from rest_framework.viewsets  import ModelViewSet
from .models import Hudud, QurilishTashkiloti, QurilishBino
from .serializers import HududSerializer, QurilishTashkilotiSerializer, QurilishBinoSerializer
from .permissions import HududPermission, QurilishTashkilotPermission, QurilishBinoPermission



class HududViewSet(ModelViewSet):
    queryset = Hudud.objects.all()
    serializer_class = HududSerializer
    permission_classes = [HududPermission]


class QurilishTashkilotiViewSet(ModelViewSet):
    queryset = QurilishTashkiloti.objects.all()
    serializer_class = QurilishTashkilotiSerializer
    permission_classes = [QurilishTashkilotPermission]


class QurilishBinoViewSet(ModelViewSet):
    queryset = QurilishBino.objects.all()
    serializer_class = QurilishBinoSerializer
    permission_classes = [QurilishBinoPermission]