from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser

from .models import *
from .serializers import KeeperSerializer


# class KeeperViewSet(viewsets.ModelViewSet):
#     queryset = Keeper.objects.all()
#     serializer_class = KeeperSerializer

class KeeperAPIList(generics.ListCreateAPIView):
    queryset = Keeper.objects.all()
    serializer_class = KeeperSerializer
    permission_classes = (IsAdminUser,)


class KeeperAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Keeper.objects.all()
    serializer_class = KeeperSerializer
    permission_classes = (IsAdminUser,)


class KeeperAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Keeper.objects.all()
    serializer_class = KeeperSerializer
    permission_classes = (IsAdminUser,)