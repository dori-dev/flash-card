from django.urls import path
from rest_framework import routers

from question import views


app_name = 'question'
urlpatterns = [
    path('answer/<int:pk>/', views.AnswerAPIView.as_view()),
]

router = routers.SimpleRouter()
router.register('', views.QuestionViewSet)
urlpatterns += router.urls
