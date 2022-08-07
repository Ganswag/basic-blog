from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Article(models.Model):

    class PublicationType(models.TextChoices):
        READS = "lecturas", "Lecturas"
        VIDEOS = "videos", "Videos"
        KAHOOT = "kahoots", "Kahoots"

    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name="Título", max_length=200)
    main_picture = models.ImageField(
        upload_to='Articles/', verbose_name="Foto de portada",
        null=True, blank=True 
    )
    slug = models.SlugField(max_length=250, unique=True)
    short_description = models.CharField(
        verbose_name='Descripción', null=False, max_length=300
    )
    publication_type = models.CharField(
        verbose_name='Tipo de publicación', null=False, max_length=12,
        choices=PublicationType.choices
    )
    resource_url = models.URLField(
        verbose_name="URL del recurso", null=False
    )
    subject = models.CharField(
        verbose_name='Materia relacionada', null=False, max_length=250
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
        verbose_name = "Recurso"
        verbose_name_plural = "Recursos"
        ordering = ['updated_at', 'title']

    def __str__(self):
        return self.title
