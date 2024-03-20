from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Student(models.Model):
    CHOICES = (
        ("MALE","MALE"),
        ("FEMALE","FEMALE"),
        ("OTHER","OTHER"),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.FileField(upload_to='profile_image/Student/',null=True,blank=True)
    gender = models.CharField(blank=False,null=False,max_length=10,choices=CHOICES)
    # date_of_birth = models.DateTimeField()
    address = models.CharField(max_length=40)
    contact_no = models.CharField(max_length=10,null=False)
    

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name