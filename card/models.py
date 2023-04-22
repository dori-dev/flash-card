from django.db import models


class FlashCard(models.Model):
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
