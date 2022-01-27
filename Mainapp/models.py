from unicodedata import category
from django.db import models

# Create your models here.

class Total_Board(models.Model):
    tb_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    type = models.CharField(max_length=45, null=False)
    category = models.CharField(max_length=45, null=False)
    writer = models.CharField(max_length=45, null=False)
    tb_date = models.DateTimeField(null=False, auto_now_add=True)
    contents = models.TextField(null=False)
    view = models.PositiveIntegerField(null=False, default=0)
    like = models.IntegerField( null=False, default=0)
    
    def summary(self):
        return self.contents[:100]
        
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'Total_Board'
        managed = False

class Total_Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    tb_no = models.ForeignKey('Total_Board', on_delete=models.CASCADE, db_column='tb_no')
    c_date = models.DateTimeField(null=False, auto_now_add=True)
    contents = models.CharField(max_length=500, null=False)
    writer = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Total_Comment'
        managed = False


class Class_Board(models.Model):
    cb_id = models.AutoField(primary_key=True)
    cb_date = models.DateTimeField(null=False)
    subject = models.CharField(max_length=150, null=True)
    today_class = models.CharField(max_length=150, null=True)
    message = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'Class_Board'
        managed = False

class Total_Scrap(models.Model):
    s_no = models.AutoField(primary_key=True)
    tb_no = models.ForeignKey('Total_Board', on_delete=models.CASCADE, db_column='tb_no')
    writer = models.CharField(max_length=45, null=False)
    category = models.CharField(max_length=45, null=False)
    s_date = models.DateTimeField(null=False, auto_now_add=True)
    class Meta:
        db_table = 'Total_Scrap'
        managed = False


class Total_Like_Board(models.Model):
    l_no = models.AutoField(primary_key=True)
    tb_no = models.ForeignKey('Total_Board', on_delete=models.CASCADE, db_column='tb_no')
    writer = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Total_Like_Board'
        managed = False