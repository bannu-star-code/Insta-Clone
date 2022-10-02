from django.contrib.auth.models import BaseUserManager
# from django.utils.translation import ugettext_lazy 
from django.utils.translation import gettext_lazy 
# to convert text in international country language
# UserManager is default django custom class to manage 
# we simply inherit and add some features

class CustomUserManager(BaseUserManager) :

    def create_user(self, email, password, username, **extra_fields):
        if not email:
            raise ValueError(gettext_lazy('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(gettext_lazy('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, username, **extra_fields)     


