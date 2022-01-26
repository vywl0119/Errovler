from django.db import models

# Create your models here.

class Board(models.Model):
    b_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=45, null=False)
    writer = models.CharField(max_length=45, null=False)
    b_date = models.DateTimeField(null=False, auto_now_add=True)
    contents = models.TextField(null=False)
    view = models.PositiveIntegerField(null=False, default=0)
    like = models.IntegerField( null=False, default=0)
    
    def summary(self):
        return self.contents[:100]
    
    # @property
    # def update_counter(self):
    #     self.view += 1
    #     self.save()

    class Meta:
        db_table = 'Board'
        managed = False


class QnA_Board(models.Model):
    qna_no = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=45, null=False)
    qna_yn = models.CharField(max_length=10, null=False, default='N')
    writer = models.CharField(max_length=45, null=False)
    qna_date = models.DateTimeField(null=False, auto_now_add=True)
    contents = models.TextField(null=False)
    view = models.PositiveIntegerField(null=False, default=0)
    like = models.IntegerField( null=False, default=0)
    
    # @property
    # def update_counter(self):
    #     self.view += 1
    #     self.save()

    class Meta:
        db_table = 'QnA_Board'
        managed = False

    def summary(self):
        return self.contents[:100]

class Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    c_date = models.DateTimeField(null=False, auto_now_add=True)
    contents = models.CharField(max_length=500, null=False)
    writer = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Comment'
        managed = False


class Scrap(models.Model):
    s_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    writer = models.CharField(max_length=45, null=False)
    class Meta:
        db_table = 'Scrap'
        managed = False

class Photo_Board(models.Model):
    s_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    filename = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = 'Photo_Board'
        managed = False



class Like_Board(models.Model):
    l_no = models.AutoField(primary_key=True)
    b_no = models.ForeignKey('Board', on_delete=models.CASCADE, db_column='b_no')
    qna_no = models.ForeignKey('QnA_Board', on_delete=models.CASCADE, db_column='qna_no')
    writer = models.CharField(max_length=45, null=False)

    class Meta:
        db_table = 'Like_Board'
        managed = False