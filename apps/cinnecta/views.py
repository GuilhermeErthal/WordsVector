from rest_framework import viewsets


from .models import Texts
from .serializers import TextsSerializer

"""
API V1
"""


class TextsViewSet(viewsets.ModelViewSet):
    queryset = Texts.objects.all()
    serializer_class = TextsSerializer


