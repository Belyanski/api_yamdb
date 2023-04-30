from django.urls import include, path
from rest_framework import routers

from api.views import (TokenView,
                       UserRegView,
                       UsersViewSet)

router1 = routers.SimpleRouter

router1.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router1.urls)),
    path('v1/auth/signup/', UserRegView.as_view()),
    path('v1/auth/token/', TokenView.as_view()),
]
