from django.conf.urls import include
from django.urls import path
from django.contrib.auth import get_user_model
from rest_framework.routers import DefaultRouter
from djoser import views as djoser_views
from .import views


User = get_user_model()

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/users/create', djoser_views.UserCreateView.as_view()),
    path('auth/users/{0}'.format(User.USERNAME_FIELD), djoser_views.SetUsernameView.as_view()),
    path('auth/users/delete', djoser_views.UserDeleteView.as_view()),
    path('auth/users/activate', djoser_views.ActivationView.as_view()),
    path('auth/password', djoser_views.SetPasswordView.as_view()),
    path('auth/password/reset', djoser_views.PasswordResetView.as_view()),
    path('auth/password/reset/confirm', djoser_views.PasswordResetConfirmView.as_view()),
    path('auth/', include('djoser.urls.jwt'))
]