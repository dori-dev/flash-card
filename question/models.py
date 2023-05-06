from random import choices
from string import ascii_letters

from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class Question(models.Model):
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='questions',
    )
    content = models.TextField()
    grade = models.PositiveSmallIntegerField()
    slug = models.SlugField(
        max_length=8,
        null=True,
        blank=True,
        unique=True,
    )
    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = (
            'content',
            '-grade',
        )

    def __str__(self) -> str:
        return f"{self.content[:100]}..."

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._return_unique_slug()
        return super().save(*args, **kwargs)

    def _return_unique_slug(self):
        self.a = 5
        while self._check_slug(slug := self._generate_slug()):
            continue
        return slug

    def _generate_slug(self, length=8):
        return "".join(choices(ascii_letters, k=length))

    def _check_slug(self, slug):
        return Question.objects.filter(slug=slug).exists()


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name='answers',
    )
    content = models.TextField()
    created = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = (
            'content',
        )

    def __str__(self) -> str:
        return f"{self.content[:100]}..."
