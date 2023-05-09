from django.test import TestCase
from django.contrib.auth import get_user_model
from model_bakery import baker

from question.models import Question, Answer


User = get_user_model()


class TestQuestion(TestCase):
    @classmethod
    def setUp(cls):
        baker.make(Question, content='Hello this is a test content.')

    def test_model_string(self):
        content = 'Hello this is a test content.'
        question = Question.objects.first()
        self.assertEqual(
            f'{content[:100]}...',
            str(question),
        )
