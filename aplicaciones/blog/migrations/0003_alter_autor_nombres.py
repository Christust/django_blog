# Generated by Django 4.1.1 on 2022-10-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_autor_nombres"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autor",
            name="nombres",
            field=models.CharField(max_length=50, verbose_name="Nombres del Autor"),
        ),
    ]
