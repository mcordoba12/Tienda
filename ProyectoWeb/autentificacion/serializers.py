from rest_framework import serializers
from django.contrib.auth.models import User  # o el modelo de usuario que estés usando
from django.contrib.auth.password_validation import validate_password

class RegistroSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    is_admin = serializers.BooleanField(write_only=True, required=False, default=False)  # Nuevo campo opcional

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'password2', 'is_admin')

    def validate(self, attrs):
        # Validar si las contraseñas coinciden
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return attrs

    def create(self, validated_data):
        # Eliminar el campo `is_admin` del validated_data antes de crear el usuario
        is_admin = validated_data.pop('is_admin', False)

        # Crear el usuario
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])

        # Asignar permisos administrativos si is_admin es True
        if is_admin:
            user.is_staff = True
            user.is_superuser = True

        user.save()
        return user
