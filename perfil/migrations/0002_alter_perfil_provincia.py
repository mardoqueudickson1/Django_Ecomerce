# Generated by Django 4.0.2 on 2022-02-11 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='provincia',
            field=models.CharField(choices=[('L', 'Luanda'), ('U', 'Uige'), ('U', 'Huambo'), ('B', 'Benguela'), ('C', 'Cabinda')], default='L', max_length=1),
        ),
    ]