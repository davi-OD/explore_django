from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add=True)
    # img = models.ImageField(upload_to="images/")

    # renames the instances of the model
    def __str__(self):
        return self.first_name
    

# # Used to add fields to the user model defaulted
# class CustomUser(AbstractUser):
#     date_of_birth = models.DateField()
#     address = models.CharField(max_length=30,blank=True)
#     bio_info = models.TextField(max_length=200)

#     def __str__(self):
#         return self.email
    

# # Used for authentication functionality
# # changing authentication from username to email 
# class Customuser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name= 'email address',
#         max_length=255,
#         unique=True
#     )
#     date_of_birth = models.DateField()
#     is_active= models.BooleanField(default=True)
#     is_admin= models.BooleanField(default=False)

#     # objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date of birth']

