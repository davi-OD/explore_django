from django.db import models

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
