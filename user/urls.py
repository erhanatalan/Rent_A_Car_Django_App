from django.urls import path, include

# after '/user/' ...
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]


# routers
from rest_framework.routers import DefaultRouter
from .views import UserView
router = DefaultRouter()
router.register('', UserView)
urlpatterns += router.urls

