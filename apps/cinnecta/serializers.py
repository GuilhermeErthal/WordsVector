from rest_framework import serializers

from .models import Texts


class TextsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Texts
        fields = (
            'title',
            'text',
            'file',
            'criacao',
        )

