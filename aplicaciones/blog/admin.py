from django.contrib import admin
from .models import *

# Herramientas para usar import_export en el admin.site
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Se crea una clase que herede de resource.ModelResource y en la class Meta colocamos el modelo que lo usara.
class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class AutorResource(resources.ModelResource):
    class Meta:
        model = Autor

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

# Agregamos una herencia mas que es ImportExportModelAdmin y el atributo resource_class el cual es la clase rescource creada anteriormente
class CategoriaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # Agregar barra de busqueda
    search_fields = ["nombre"]
    # Lista de atributos
    list_display = ("nombre", "estado", "fecha_creacion")
    resource_class = CategoriaResource

class AutorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["nombres", "apellidos", "correo"]
    list_display = ("nombres", "apellidos", "correo", "estado", "fecha_creacion")
    resource_class = AutorResource

class PostAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["titulo", "slug", "descripcion"]
    list_display = ("titulo", "slug", "descripcion", "fecha_creacion")
    resource_class = PostResource

# Register your models here.
admin.site.register(Autor, AutorAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)