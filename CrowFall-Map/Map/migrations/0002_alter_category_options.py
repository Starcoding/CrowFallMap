# Generated by Django 4.1 on 2022-08-23 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Map", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("title",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
