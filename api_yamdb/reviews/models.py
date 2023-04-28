from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """Модель отзывов."""
    author = models.ForeignKey(
        User,
        related_name='reviews',
        on_delete=models.CASCADE,
        verbose_name='Автор отзыва',
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение для оценки'
    )
    text = models.TextField('Ваш отзыв')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True,
    )
    score = models.PositiveSmallIntegerField(
        'Оценка произведения',
        validators=[
            MinValueValidator(1, message='Оценка должна быть от 1'),
            MaxValueValidator(10, message='Оценка должна быть до 10')
        ]
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name='unique follow'
            )
        ]
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]


class Comments(models.Model):
    """Модель комментариев."""
    author = models.ForeignKey(
        User,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Автор комментария'
    )
    review = models.ForeignKey(
        Review,
        related_name='comments',
        on_delete=models.CASCADE,
        verbose_name='Комментируемый отзыв'
    )
    text = models.TextField('Ваш комментарий')
    pub_date = models.DateTimeField(
        'Дата комментария',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.text[:15]
