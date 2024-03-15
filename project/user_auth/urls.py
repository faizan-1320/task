from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('register/', views.RegiserView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('', include(router.urls)),
]