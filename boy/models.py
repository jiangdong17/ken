#coding = utf-8
from django.db import models
from django.utils.encoding import force_bytes

# Create your models here.

class Schools(models.Model):
    #sid = models.IntegerField()
    sdate = models.DateField()
    sname = models.CharField(max_length=20)
    scity = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    def __str__(self):
        return self.sname

class Grades(models.Model):
    #gid = models.IntegerField()
    gyear = models.CharField(max_length=20)
    ggirlnum = models.IntegerField()
    gboynum = models.IntegerField()
    isDelete = models.BooleanField(default=False)
    gschool = models.ForeignKey("Schools",on_delete=models.CASCADE,)
    #def __str__(self):
        #return self.gyear

class Students(models.Model):
    #xid = models.IntegerField()
    xname = models.CharField(max_length=20)
    xage = models.IntegerField()
    xgender = models.BooleanField(default=False)
    xgrade = models.ForeignKey("Grades",on_delete=models.CASCADE,)
    isDelete = models.BooleanField(default=False)
    gschool = models.ForeignKey("Schools", on_delete=models.CASCADE, )
    def __str__(self):
        return self.xname

class Plans(models.Model):
    pname =models.CharField(max_length=20)
    pp_start_time = models.DateField()
    pp_long = models.IntegerField()
    pstart_time = models.DateField()
    pover_time = models.DateField()
    plong = models.IntegerField()
    pscore = models.IntegerField()
    pstudent = models.ForeignKey("Students",on_delete=models.CASCADE,)
    def __str__(self):
        return self.pname