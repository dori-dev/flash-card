from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from model_bakery import baker

from question import models


User = get_user_model()


class TestQuestionListView(TestCase):
    def setUp(self):
        self.client = Client()
        for _ in range(5):
            baker.make(models.Question)

    def test_question_list(self):
        url = reverse('question:question-list')
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['count'], 5)
        self.assertIsNone(data['next'])
        self.assertIsNone(data['previous'])
        self.assertEqual(models.Question.objects.count(), 5)


class TestQuestionCreateView(TestCase):
    def test_question_create(self):
        data = {
            'content': 'Hello this is an test content',
            'grade': 5,
        }
        access_token = self._auth()
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        url = reverse('question:question-list')
        response = self.client.post(
            url,
            data,
            'application/json',
            headers=headers,
        )
        result = response.json()
        questions = self._get_questions()
        self.assertEqual(response.status_code, 201)
        self.assertEqual(result['content'], data['content'])
        self.assertEqual(result['grade'], data['grade'])
        self.assertEqual(questions['count'], 1)
        question = questions['results'][0]
        self.assertEqual(question['id'], 1)
        self.assertEqual(question['content'], data['content'])
        self.assertEqual(question['grade'], data['grade'])
        self.assertEqual(len(question['slug']), 8)
        self.assertEqual(models.Question.objects.count(), 1)

    def test_invalid_question_create(self):
        access_token = self._auth()
        headers = {
            'Authorization': f'Bearer {access_token}',
        }
        url = reverse('question:question-list')
        response = self.client.post(
            url,
            {},
            'application/json',
            headers=headers,
        )
        result = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(len(result), 2)

    def _auth(self):
        data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': 'testpass',
        }
        User.objects.create_user(**data)
        response = self.client.post(reverse('token_obtain_pair'), data)
        return response.json().get('access')

    def _get_questions(self):
        url = reverse('question:question-list')
        response = self.client.get(url)
        return response.json()
