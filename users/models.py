from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models

from course.models import Course, Lesson


# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('У пользователя должен быть email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError('У суперпользователя is_staff должен быть True')
        if not extra_fields.get('is_superuser'):
            raise ValueError('У суперпользователя is_superuser должен быть True')

        return self.create_user(email, password, **extra_fields)


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

    objects = CustomUserManager()

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


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subscriptions')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']

    def __str__(self):
        return f'{self.user.email} → {self.course.title}'