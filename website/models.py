from django.db import models


# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(
        auto_now=False, auto_now_add=True, null=False, blank=False
    )
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=50, null=False, blank=False)
    zipcode = models.BigIntegerField(null=False, blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
