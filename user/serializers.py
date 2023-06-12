from rest_framework import serializers


# userserializer
from django.contrib.auth.models import User
# ayni email ile birden fazla kisi uye olmasin diye
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    # email zorunlu hale geliyor
    email = serializers.EmailField(
        required = True,
        validators = [UniqueValidator(
            queryset=User.objects.all()
            )
        ]
    )

    password = serializers.CharField(
        required = False,
        write_only = True,
    )
    class Meta:
        model = User
        exclude = [
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]
    
    # sifre degistirme de otomatik validate islemi saglar
    def validate(self, attrs):
        if attrs.get('password', False):
            from django.contrib.auth.password_validation import validate_password
            from django.contrib.auth.hashers import make_password
            password = attrs['password']
            validate_password(password)
            attrs.update({'password': make_password(password)})
        return super().validate(attrs)

# UserTokenSerializer
# -------------------------------
from dj_rest_auth.serializers import TokenSerializer

class UserTokenSerializer(TokenSerializer):
    user = UserSerializer()
    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')