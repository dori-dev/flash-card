from django.test import SimpleTestCase
from django.urls import reverse, resolve
from question.views import AnswerAPIView, QuestionViewSet


class TestUrls(SimpleTestCase):
    def test_answer(self):
        url = reverse('question:answer', args=(1,))
        self.assertEqual(
            resolve(url).func.cls,
            AnswerAPIView,
        )

    def test_question_list(self):
        url = reverse('question:question-list')
        self.assertEqual(
            resolve(url).func.cls,
            QuestionViewSet,
        )

    def test_question_detail(self):
        url = reverse('question:question-detail', args=(1,))
        self.assertEqual(
            resolve(url).func.cls,
            QuestionViewSet,
        )
