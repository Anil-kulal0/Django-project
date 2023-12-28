# myapp/views.py

from rest_framework import generics, permissions
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import CustomUser
from .serializers import UserSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        # Send verification email
        user = CustomUser.objects.get(email=request.data['email'])
        self.send_verification_email(user)

        return response

    def send_verification_email(self, user):
        subject = 'Verify Your Email'
        message = f'Hello'
        from_email = 'anilkulal1212@gmail.com'  # Replace with your email address
        recipient_list = [user.email]
        send_mail(subject, message, from_email, recipient_list)

