from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course, Lesson


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="email address")
    phone = models.CharField(
        max_length=20, blank=True, null=True, verbose_name="phone number"
    )
    city = models.CharField(max_length=20, blank=True, null=True, verbose_name="city")
    avatar = models.ImageField(
        upload_to="users/avatars", null=True, blank=True, verbose_name="avatar"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class PaymentMethod(models.Model):
    name = models.CharField(max_length=20, verbose_name="Вид оплаты")


class Payment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    payment_date = models.DateField(null=True, blank=True, verbose_name="Дата платежа")
    payed_course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Оплаченный курс",
    )
    payed_lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Отдельно оплаченный урок",
    )
    payment_amount = models.IntegerField(
        null=True, blank=True, verbose_name="Сумма платежа"
    )
    payment_method = models.ForeignKey(
        PaymentMethod,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Вид оплаты",
    )
