# Generated by Django 4.1 on 2022-08-23 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Map", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dot",
            name="category",
            field=models.ManyToManyField(blank=True, to="Map.category"),
        ),
    ]
