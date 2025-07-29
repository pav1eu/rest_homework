from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from course.serializers import PaymentSerializer
from users.models import Payment


# Create your views here.
class PaymentListView(generics.ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["payed_course", "payed_lesson", "payment_method"]
    ordering_fields = ["payment_date"]
    ordering = ["-payment_date"]
