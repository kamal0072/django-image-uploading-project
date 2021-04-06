from django.db import models

class UserImage(models.Model):
    pics=models.ImageField(upload_to='userimages')
    date=models.DateTimeField(auto_now_add=True)
    