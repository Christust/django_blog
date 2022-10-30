from django.shortcuts import render, get_object_or_404
from .models import *
# Q se utiliza para hacer consultas con logica como and's y or's
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        # distinct se usa para no repetir objetos ya que el filtro puede traer dos mismos elementos
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            estado = True
        ).distinct()
    # Instanciamos paginator
    paginator = Paginator(posts, 2)
    # Generamos una variable llamada page que obtenemos de request
    page = request.GET.get("page")
    # Redefinimos posts para mandar solo los que debemos segun la paginacion
    posts = paginator.get_page(page)
    context = {"posts":posts}
    return render(request, "index.html", context)

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    context = {"post":post}
    return render(request, "post.html", context)

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact ="General"))
    if queryset:
        # distinct se usa para no repetir objetos ya que el filtro puede traer dos mismos elementos
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            categoria = Categoria.objects.get(nombre__iexact ="General"),
            estado = True
        ).distinct()
     # Instanciamos paginator
    paginator = Paginator(posts, 2)
    # Generamos una variable llamada page que obtenemos de request
    page = request.GET.get("page")
    # Redefinimos posts para mandar solo los que debemos segun la paginacion
    posts = paginator.get_page(page)
    context = {"posts":posts}
    return render(request, "generales.html", context)

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Programacion"))
    if queryset:
        # distinct se usa para no repetir objetos ya que el filtro puede traer dos mismos elementos
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact="Programacion")
        ).distinct()
     # Instanciamos paginator
    paginator = Paginator(posts, 2)
    # Generamos una variable llamada page que obtenemos de request
    page = request.GET.get("page")
    # Redefinimos posts para mandar solo los que debemos segun la paginacion
    posts = paginator.get_page(page)
    context = {"posts":posts}
    return render(request, "programacion.html",context)

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Tutoriales"))
    if queryset:
        # distinct se usa para no repetir objetos ya que el filtro puede traer dos mismos elementos
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact="Tutoriales")
        ).distinct()
     # Instanciamos paginator
    paginator = Paginator(posts, 2)
    # Generamos una variable llamada page que obtenemos de request
    page = request.GET.get("page")
    # Redefinimos posts para mandar solo los que debemos segun la paginacion
    posts = paginator.get_page(page)
    context = {"posts":posts}
    return render(request, "tutoriales.html",context)

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Tecnologia"))
    if queryset:
        # distinct se usa para no repetir objetos ya que el filtro puede traer dos mismos elementos
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact="Tecnologia")
        ).distinct()
     # Instanciamos paginator
    paginator = Paginator(posts, 2)
    # Generamos una variable llamada page que obtenemos de request
    page = request.GET.get("page")
    # Redefinimos posts para mandar solo los que debemos segun la paginacion
    posts = paginator.get_page(page)
    context = {"posts":posts}
    return render(request, "tecnologia.html",context)

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Videojuegos"))
    if queryset:
        # distinct se usa para no repetir objetos ya que el filtro puede traer dos mismos elementos
        posts = Post.objects.filter(
            Q(titulo__icontains= queryset) |
            Q(descripcion__icontains=queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact="Videojuegos")
        ).distinct()
     # Instanciamos paginator
    paginator = Paginator(posts, 2)
    # Generamos una variable llamada page que obtenemos de request
    page = request.GET.get("page")
    # Redefinimos posts para mandar solo los que debemos segun la paginacion
    posts = paginator.get_page(page)
    context = {"posts":posts}
    return render(request, "videojuegos.html",context)
