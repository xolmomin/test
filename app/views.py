from rest_framework.permissions import AllowAny

from app.models import New
from app.serializers import NewSerializer
from rest_framework import viewsets


class NewViewSet(viewsets.ModelViewSet):
    queryset = New.objects.all()
    serializer_class = NewSerializer
    permission_classes = (AllowAny,)
