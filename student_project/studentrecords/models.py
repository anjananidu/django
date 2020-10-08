from django.db import models

class Students(models.Model):
    Reg_no = models.CharField(max_length=20,unique = True,primary_key = True,blank = False)
    stud_name = models.CharField(max_length=100,blank = False)
    stud_email = models.EmailField(unique = True,blank = False)
    stud_phone = models.CharField(max_length=15, unique = True,blank = False)
