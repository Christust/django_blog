# Generated by Django 4.1.1 on 2022-10-23 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="nombres",
            field=models.CharField(
                max_length=50, verbose_name="Nombres del Autor en cuestion"
            ),
        ),
    ]
