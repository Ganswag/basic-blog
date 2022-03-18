from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Título", max_length=200)
    main_picture = models.ImageField(
        upload_to='Articles/', verbose_name="Foto de portada"
    )
    slug = models.SlugField(max_length=250)
    short_description = models.CharField(
        verbose_name='Descripción', null=False, max_length=300
    )
    content = RichTextField(
        verbose_name="Contenido", null=False
    )
    subject = models.CharField(
        verbose_name='Materia relacionada', null=False, max_length=250
    )
    published = models.BooleanField(
        verbose_name='Mostrar al público', null=False,
        default=False
    )
    author = models.ForeignKey(
        User, on_delete=models.DO_NOTHING,
        verbose_name='Autor', null=False
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación", null=False,
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Fecha de creación", null=False,
        auto_now=True
    )

    class Meta:
        verbose_name = "artículo"
        verbose_name_plural = "artículos"
        ordering = ['updated_at', 'title']

    def __str__(self):
        return self.title
