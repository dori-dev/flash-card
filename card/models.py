from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class FlashCard(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='cards',
    )
    question = models.TextField()
    answer = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
    )
    updated = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self) -> str:
        string = " ".join(
            self.question[:30].split()[:-1]
        )
        return f"{string}..."
