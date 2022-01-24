from django.db import models

# Create your models here.


class Member(models.Model):
    id = models.CharField(max_length=45,  primary_key=True)
    pw = models.CharField(max_length=45, null=False)
    nickname = models.CharField(max_length=45, null=False)
   
    class Meta:
        db_table = 'Member'
        app_label = 'Mainapp'
        managed = False


class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=45, null=False)
    id = models.CharField(max_length=45, null=False)
    b_date = models.DateTimeField(null=False)
    contents = models.TextField(null=False)
    view = models.IntegerField(null=False)
    like = models.IntegerField( null=False)

    class Meta:
        db_table = 'Board'
        app_label = 'Boardapp'
        managed = False


class QnA_Board(models.Model):
    qna_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=45, null=False)
    qna_yn = models.CharField(max_length=10, null=False)
    id = models.CharField(max_length=45, null=False)
    qna_date = models.DateTimeField(null=False)
    contents = models.TextField(null=False)
    view = models.IntegerField(null=False)
    like = models.IntegerField( null=False)

    class Meta:
        db_table = 'QnA_Board'
        app_label = 'Boardapp'
        managed = False

class Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    b_no = models.IntegerField(null=True)
    qna_no = models.IntegerField(null=True)
    qna_date = models.DateTimeField(null=False)
    contents = models.CharField(max_length=500, null=False)
    id = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Comment'
        app_label = 'Boardapp'
        managed = False


class Scrap(models.Model):
    s_no = models.AutoField(primary_key=True)
    b_no = models.IntegerField(null=True)
    qna_no = models.IntegerField(null=True)
    id = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Scrap'
        app_label = 'Boardapp'
        managed = False

class Photo_Board(models.Model):
    s_no = models.AutoField(primary_key=True)
    b_no = models.IntegerField(null=True)
    qna_no = models.IntegerField(null=True)
    filename = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'Photo_Board'
        app_label = 'Boardapp'
        managed = False



class Like_Board(models.Model):
    l_no = models.AutoField(primary_key=True)
    b_no = models.IntegerField(null=True)
    qna_no = models.IntegerField(null=True)
    id = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Like_Board'
        app_label = 'Boardapp'
        managed = False