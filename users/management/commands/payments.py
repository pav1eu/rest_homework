from django.core.management.base import BaseCommand
from users.models import User, Payment, PaymentMethod
from course.models import Course, Lesson
from django.utils.timezone import now


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        Payment.objects.all().delete()
        PaymentMethod.objects.all().delete()

        Payment.objects.all().delete()
        PaymentMethod.objects.all().delete()

        method_cash = PaymentMethod.objects.create(name="Наличные")
        method_transfer = PaymentMethod.objects.create(name="Перевод на счет")

        payment_methods = [method_cash, method_transfer]

        users = User.objects.all()
        courses = Course.objects.all()
        lessons = Lesson.objects.all()

        payment = Payment.objects.create(
            user=users[0],
            payed_lesson=None,
            payed_course=courses[0],
            payment_date=now(),
            payment_amount=5000,
            payment_method=method_cash,
        )
