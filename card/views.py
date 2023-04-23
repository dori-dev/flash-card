from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from card.models import FlashCard
from card.permissions import IsOwnerOrReadOnly
from card.serializers import FlashCardSerializer


class CreateListFlashCardView(APIView):
    serializer_class = FlashCardSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly,
    ]

    def get(self, request):
        flash_cards = FlashCard.objects.all()
        serializer = self.serializer_class(
            flash_cards,
            many=True,
        )
        return Response({
            "count": flash_cards.count(),
            "data": serializer.data,
        })

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )


# Create your views here.
