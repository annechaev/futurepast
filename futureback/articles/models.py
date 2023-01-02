from django.db import models
from django_extensions.db.models import AutoSlugField

# Create your models here.


class Articles(models.Model):

    title = models.CharField(max_length=255, verbose_name="Заголовок")
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    image_top = models.ImageField(upload_to="images_top/%Y/%m/%d/")
    views = models.BigIntegerField()
    slug = AutoSlugField(populate_from='title', unique=True, db_index=True)
    author_id = models.ForeignKey('Authors', on_delete=models.PROTECT, null=True)
    category_id = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Authors(models.Model):

    name = models.CharField(max_length=255, verbose_name="Имя")
    slug = AutoSlugField(populate_from='name', unique=True)

    def __str__(self):
        return self.name


class Categories(models.Model):

    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title', unique=True)

    def __str__(self):
        return self.title
