from django.conf import settings
from django.db import models


# Create your models here.
class Course(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_courses')
    title = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(
        upload_to="course/preview", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Lesson(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='my_lessons')
    title = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(
        upload_to="course/preview", blank=True, null=True, verbose_name="Превью"
    )
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    video_url = models.URLField(verbose_name="Ссылка на видео", blank=True, null=True)

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
