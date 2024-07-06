from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import random
import string
from django.urls import reverse
from django.views import View

User = get_user_model()

class PasswordResetView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'components/password_reset.html', {'title1': 'Recuperar Contraseña'})
    
    def post(self, request, *args, **kwargs):
        try:
            email = request.POST['email']
            user = User.objects.get(email=email)
            
            # Generar contraseña aleatoria
            new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
            user.set_password(new_password)
            user.save()
            
            # Enviar email
            send_mail(
                'Tu nueva contraseña',
                f'Tu nueva contraseña es: {new_password}',
                'noreply@tudominio.com',
                [email],
                fail_silently=False,
            )
            
            messages.success(request, 'Se ha enviado una nueva contraseña a tu correo.')
            return redirect(reverse('security:auth_login'))  # Redirigir al login después de enviar la nueva contraseña
        except User.DoesNotExist:
            messages.error(request, 'El correo no se encuentra registrado.')
        
        return render(request, 'components/password_reset.html', {'title1': 'Recuperar Contraseña'})