import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

def rename_img_profile(instance, filename):
    path = 'profiles/'
    # print(dir(instance))
    file_name = '{0}_{1}.{2}'.format(instance, get_random_string(length=32), filename.split(".")[-1])
    return os.path.join(path, file_name)

class Funcionario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=rename_img_profile, blank=True, null=True)

    def __str__(self):
        return self.user.first_name