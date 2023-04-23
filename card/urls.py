from django.urls import path

from card import views

app_name = 'card'
urlpatterns = [
    path(
        '',
        views.CreateListFlashCardView.as_view(),
        name='create_list',
    ),
    path(
        '<int:pk>/',
        views.RetrieveUpdateDeleteFlashCardView.as_view(),
        name='detail_update_delete',
    ),
]
