# Generated by Django 4.0.2 on 2022-03-07 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0013_alter_produto_preco_promocional'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variacao',
            name='preco_promocional',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='Preço promocional'),
        ),
    ]