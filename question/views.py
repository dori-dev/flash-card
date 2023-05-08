from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

from question import models, serializers
from permissions import IsOwnerOrReadOnly


class QuestionViewSet(viewsets.ModelViewSet, LimitOffsetPagination):
    queryset = models.Question.objects
    serializer_class = serializers.QuestionSerializer
    permission_classes = [
        IsOwnerOrReadOnly,
    ]

    def list(self, request):
        questions = self.paginate_queryset(self.queryset.all())
        serializer = self.serializer_class(
            instance=questions,
            many=True,
        )
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(user=request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        question = get_object_or_404(models.Question, pk=pk)
        serializer = self.serializer_class(instance=question)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, pk=None):
        question = get_object_or_404(models.Question, pk=pk)
        self.check_object_permissions(request, question)
        serializer = self.serializer_class(
            instance=question,
            data=request.data,
            partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        question = get_object_or_404(models.Question, pk=pk)
        self.check_object_permissions(request, question)
        question.delete()
        return Response(status=status.HTTP_200_OK)


class AnswerAPIView(APIView):
    serializer_class = serializers.AnswerSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, pk=None):
        question = get_object_or_404(models.Question, pk=pk)
        serializer = self.serializer_class(
            instance=question.answers,
            many=True,
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        question = get_object_or_404(models.Question, pk=pk)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(question=question)
        return Response(serializer.data, status.HTTP_201_CREATED)
