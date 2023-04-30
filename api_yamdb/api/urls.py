from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from api.views import (TokenView,
                       UserRegView,
                       UsersViewSet)

router1 = routers.SimpleRouter()

router1.register('users', UsersViewSet, basename='users')

urlpatterns = [
    path('v1/', include(router1.urls)),
    path('v1/auth/', include([
        path('signup/', UserRegView.as_view()),
        path('token/', TokenView.as_view())
    ])),
    path('token/', TokenObtainPairView.as_view())
]
