from django.db import models

class Row(models.Model):
    """
    Строка таблицы
    """
    date = models.DateField(verbose_name="Дата")
    name = models.CharField(
        max_length=30,
        verbose_name="Название"
    )
    quantity = models.FloatField(verbose_name="Количество")
    distance = models.FloatField(verbose_name="Расстояние")

    def __str__(self):
        return str(self.name)
