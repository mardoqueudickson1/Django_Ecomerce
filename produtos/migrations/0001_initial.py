# Generated by Django 4.0.2 on 2022-02-09 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('descricao_curta', models.TextField(max_length=255)),
                ('descricao_longa', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='imagem/%Y/%m/')),
                ('slug', models.SlugField()),
                ('preco', models.FloatField()),
                ('preco_promocional', models.FloatField(default=0)),
                ('tipo', models.CharField(choices=[('X', 'Variação'), ('S', 'Simples')], default='X', max_length=1)),
            ],
        ),
    ]
