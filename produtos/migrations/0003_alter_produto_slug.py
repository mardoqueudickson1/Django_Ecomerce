# Generated by Django 4.0.2 on 2022-02-10 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_variacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]