from .serializers import (
    User, 
    UserSerializer,
)

# userview
from rest_framework.viewsets import ModelViewSet

class UserView():
    qeryset = User.objects.all()
    serializer_class = UserSerializer
    