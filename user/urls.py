from django.urls import path, include

# after '/user/' ...
urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
]