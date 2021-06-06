from django.db import models
import datetime
# Create your models here.

class FileCategory(models.Model):
    categoryName = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.categoryName
    class Meta:
        verbose_name_plural = "File Categories"


class FileSubcategory(models.Model):
    subcatName = models.CharField(max_length=100)
    catName = models.ForeignKey(FileCategory, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.subcatName
    class Meta:
        verbose_name_plural = "File Subcategories"


class Files(models.Model):
    subcat = models.ForeignKey(FileSubcategory, on_delete=models.CASCADE)
    file = models.FileField(upload_to='')
    uploaded_on = models.DateTimeField(
        auto_now_add=True)
    
    class Meta:
        verbose_name_plural = "Files"

    def __str__(self) -> str:
        return str(self.subcat)
