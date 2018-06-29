from django.db import models

# Create your models here. 
class DpyTable(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=12)
    def __str__(self):
            return self.username
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=18, blank=True, null=True)
    mobile_number = models.CharField(db_column='MobileNumber', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adhaar_number = models.CharField(db_column='AdhaarNumber', max_length=12, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dpy_table'
