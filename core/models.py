from ckeditor.fields import RichTextField
from django.db import models


class SiteData(models.Model):
    site_name = models.CharField(
        verbose_name="Nombre del sitio", max_length=50, null=False)
    favicon = models.ImageField(
        upload_to='site/favicon/', verbose_name="Favicon",
        null=True, blank=True)
    logo = models.ImageField(
        upload_to='site/logos/', verbose_name="Logo del sitio",
        null=True, blank=True)
    main_image = models.ImageField(
        upload_to='site/images/', verbose_name="Portada del sitio",
        null=True, blank=True)
    site_description = models.CharField(
        verbose_name="Descripción del sitio",
        max_length=500, null=False)
    google_tag = models.CharField(
        verbose_name="Site Tag Google", max_length=50, null=True, blank=True)
    facebook_pixel = models.CharField(
        verbose_name="Pixel de Facebook", max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'Información del Sitio'
        verbose_name_plural = 'Información del Sitio'
        ordering = ['updated_at']


class ContentManagmentSystem(models.Model):
    slug = models.SlugField(max_length=250, primary_key=True)
    title = models.CharField(verbose_name="Título", max_length=200)
    main_picture = models.ImageField(
        upload_to='CMS/', verbose_name="Foto de portada"
    )
    content = RichTextField(
        verbose_name="Contenido", null=False
    )
    created_at = models.DateTimeField(
        verbose_name="Fecha de creación", auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        verbose_name = 'pagina estática'
        verbose_name_plural = 'paginas estáticas'
        ordering = ['title']

    def __str__(self):
        return self.title
