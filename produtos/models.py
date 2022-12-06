from django.db import models
from django.conf import settings
from PIL import Image
import os
from django.utils.text import slugify



class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255, verbose_name='Descrição curta')
    descricao_longa = models.TextField()
    imagem = models.ImageField(upload_to='produto_imagem/%Y/%m')
    imagem1 = models.ImageField(upload_to='produto_imagem/%Y/%m', blank=True, null=True)
    imagem2 = models.ImageField(upload_to='produto_imagem/%Y/%m', blank=True, null=True)
    imagem3 = models.ImageField(upload_to='produto_imagem/%Y/%m', blank=True, null=True)
    
    slug = models.SlugField(unique=True, blank=True, null=True)
    preco_marketing = models.FloatField(verbose_name='Preço')
    preco_promocional = models.FloatField(default=0, blank=True, null=True, verbose_name='Preço Promo.')
    tipo = models.CharField(
        default='V',
        max_length=1,
        choices=(
            ('V', 'Variável'),
            ('S', 'simples'),
        )
    )


    # FORMATAÇÃO DO PREÇO
    def get_preco_formatado(self):
        return f'Kz{self.preco:qs:.2f}'

    get_preco_formatado.short_description = 'Preço'



    # REDIRECIONAMETO DE IMAGENS

    @staticmethod
    def resize_image(img, new_width=800):
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
        img_pil = Image.open(img_full_path)
        origial_width, original_heigth = img_pil.size

        if origial_width <= new_width:
            img_pil.close()
            return

        new_heigth = round((new_width * original_heigth)  / origial_width)

        new_img = img_pil.resize((new_width, new_heigth), Image.LANCZOS)
        new_img.save(
            img_full_path,
            optimize=True,
            quality=50
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = slugify(self.nome)
            self.slug = slug

        super().save(*args, **kwargs)

        max_image_size = 800

        if self.imagem:
            self.resize_image(self.imagem, max_image_size)

    def __str__(self):
        return self.nome



class Variacao(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    nome =  models.CharField(max_length=50, blank=True, null=True)
    preco = models.FloatField(verbose_name='preço')
    preco_promocional = models.FloatField(default=0, blank=True, null=True, verbose_name='Preço promocional')
    estoque = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.nome or self.produto.nome

    class Meta:
        verbose_name = 'Variação'
        verbose_name_plural = 'Variações'
    