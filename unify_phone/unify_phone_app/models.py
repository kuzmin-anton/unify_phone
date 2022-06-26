from django.db import models

# Create your models here.
class Phone(models.Model):
    phone = models.CharField("Телефон", max_length=255)

    class Meta:
        db_table = 'phone'