from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.


class Member(models.Model):
    id = CharField(max_length=45,  primary_key=True)
    pw = CharField(max_length=45, null=False)
    nickname = CharField(max_length=45, null=False)
   
    class Meta:
        db_table = 'Member'
        app_label = 'Mainapp'
        managed = False