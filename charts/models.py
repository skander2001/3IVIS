from django.db import models

# Create your models here.
class SalesData(models.Model):
    month = models.CharField(max_length=20)
    sales = models.IntegerField()

    def __str__(self):
        return f"{self.month}: {self.sales}"