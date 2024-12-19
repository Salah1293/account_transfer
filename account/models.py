from django.db import models
import uuid

# Create your models here.


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, db_index=True)
    name = models.CharField(max_length=200)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name} has {self.balance}'
