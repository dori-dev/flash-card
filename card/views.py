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


class RetrieveUpdateDeleteFlashCardView(APIView):
    serializer_class = FlashCardSerializer
    permission_classes = [
        IsAuthenticatedOrReadOnly &
        IsOwnerOrReadOnly
    ]

    def dispatch(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.flash_card = get_object_or_404(
            FlashCard,
            pk=pk,
        )
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, pk):
        serializer = self.serializer_class(
            self.flash_card,
        )
        return Response(data=serializer.data)

    def put(self, request, pk):
        serializer = self.serializer_class(
            instance=self.flash_card,
            data=request.data,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        self.flash_card.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
