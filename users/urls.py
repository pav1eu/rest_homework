from django.urls import path


from users.views import PaymentListView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path("", PaymentListView.as_view(), name="payment-list"),
]
