from django.db import models
import datetime
# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class FileCategory(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.categoryName


class FileSubcategory(models.Model):
    subcatName = models.CharField(max_length=100)
    catName = models.ForeignKey(FileCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.subcatName


class Files(models.Model):
    subcat = models.ForeignKey(FileSubcategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')
    uploaded_on = models.DateTimeField(
        auto_now_add=True)

    def __str__(self) -> str:
        return str(self.subcat)
