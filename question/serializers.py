from rest_framework import serializers

from question import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = '__all__'
        read_only_fields = [
            'id',
            'user',
            'slug',
            'created',
        ]

    def create(self, **kwargs):
        self.validated_data.update(kwargs)
        return super().create(self.validated_data)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Answer
        fields = '__all__'
        read_only_fields = [
            'id',
            'question',
            'created',
        ]

    def create(self, **kwargs):
        self.validated_data.update(kwargs)
        return super().create(self.validated_data)
