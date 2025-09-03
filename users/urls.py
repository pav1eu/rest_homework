from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import PaymentListView, UserCreateAPIView, UserListView, UserDetailView, CourseSubscriptionToggleView

from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path("payment/", PaymentListView.as_view(), name="payment-list"),
    path("register/", UserCreateAPIView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("", UserListView.as_view(), name="user_list"),
    path("<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("subscribe/", CourseSubscriptionToggleView.as_view(), name="course_subscribe"),
]
