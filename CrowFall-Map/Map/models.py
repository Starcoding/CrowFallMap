from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField("Название категории", max_length=30)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("title",)


class Dot(models.Model):
    x_coordinate = models.FloatField("Х координата", max_length=10)
    y_coordinate = models.FloatField("Y координата", max_length=10)
    color = models.CharField("Цвет точки", max_length=10, blank=True)
    name = models.CharField("Название для точки", max_length=30)
    description = models.CharField("Описание для точки", max_length=100, blank=True)
    icon = models.CharField("Иконка точки", max_length=10, blank=True)
    map = models.ForeignKey("Map", verbose_name="Карта", on_delete=models.CASCADE)
    category = models.ManyToManyField("Category", blank=True)

    def __str__(self):
        return f"{self.name}: {self.description}. ->{self.map}"

    class Meta:
        verbose_name = "Точка на карте"
        verbose_name_plural = "Точки на карте"
        ordering = (
            "name",
            "description",
        )


class Map(models.Model):
    TYPES_OF_LOCATION = [
        ("wild", "Дикие земли"),
        ("siege", "Осада"),
        ("adventure", "Приключения"),
        ("temple", "Храм"),
    ]
    image = models.ImageField("Изображение карты")
    location_name = models.CharField("Название локации", max_length=30)
    type_of_location = models.CharField(
        "Тип локации локации", max_length=9, choices=TYPES_OF_LOCATION, blank=True
    )

    def __str__(self):
        return f"{self.location_name} -> {self.type_of_location}"

    class Meta:
        verbose_name = "Карта"
        verbose_name_plural = "Карты"
        ordering = (
            "location_name",
            "type_of_location",
        )
