from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        "Nombre de la categoria", max_length=150, blank=False, null=False
    )
    estado = models.BooleanField(
        "Categoria Activada/Categoria no Activada", default=True
    )
    fecha_creacion = models.DateField(
        "Fecha de creación", auto_now=False, auto_now_add=True
    )

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(
        ("Nombres del Autor"), max_length=50, null=False, blank=False
    )
    apellidos = models.CharField(
        "Apellidos del Autor", max_length=50, null=False, blank=False
    )
    facebook = models.URLField("Facebook", max_length=200, null=True, blank=True)
    twitter = models.URLField("Twitter", max_length=200, null=True, blank=True)
    instagram = models.URLField("Instagram", max_length=200, null=True, blank=True)
    web = models.URLField("Web", max_length=200, null=True, blank=True)
    correo = models.EmailField(
        "Correo electronico", max_length=254, null=False, blank=False
    )
    estado = models.BooleanField("Autor Activo/Autor no Activo", default=True)
    fecha_creacion = models.DateField(
        "Fecha de creación", auto_now=False, auto_now_add=True
    )

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return "{0},{1}".format(self.apellidos, self.nombres)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(("Titulo"), max_length=50, blank=False, null=False)
    slug = models.SlugField(("Slug"), max_length=100, blank=False, null=False)
    descripcion = models.CharField(
        ("Descripción"), max_length=110, blank=False, null=False
    )
    contenido = RichTextField()
    imagen = models.URLField(("Imagen"), max_length=255, blank=False, null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(("Publicado/No publicado"), default=True)
    fecha_creacion = models.DateField(
        ("Fecha de creación"), auto_now=False, auto_now_add=True
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.titulo
