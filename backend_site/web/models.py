from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    class_object = models.CharField("Класс", max_length=150)
    description = models.TextField("Описание обьекта")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Car(models.Model):
    name_car = models.CharField("Категория", max_length=40)
    status_active = models.BooleanField()
    description = models.TextField("Описание авто")

    #image = models.ImageField("Изображение машины", upload_to="images_store/")

    def __str__(self):
        return self.name_car

    class meta:
        verbose_name = "автомобили"
        verbose_name_plural = "автомобили"


