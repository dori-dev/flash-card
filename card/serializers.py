from rest_framework.serializers import ModelSerializer

from card.models import FlashCard


class FlashCardSerializer(ModelSerializer):
    class Meta:
        model = FlashCard
        fields = "__all__"
        extra_kwargs = {
            'user': {
                'read_only': True,
            },
            'created': {
                'read_only': True,
            },
            'updated': {
                'read_only': True,
            },
        }
