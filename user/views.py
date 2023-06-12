from .serializers import (
    User, 
    UserSerializer,
)

# userview
from rest_framework.viewsets import ModelViewSet

class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
