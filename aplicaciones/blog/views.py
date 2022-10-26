from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home(request):
    posts = Post.objects.filter(estado = True)
    context = {"posts":posts}
    return render(request, "index.html", context)

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    context = {"post":post}
    return render(request, "post.html", context)

def generales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact ="General"))
    context = {"posts":posts}
    return render(request, "generales.html", context)

def programacion(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Programacion"))
    context = {"posts":posts}
    return render(request, "programacion.html",context)

def tutoriales(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Tutoriales"))
    context = {"posts":posts}
    return render(request, "tutoriales.html",context)

def tecnologia(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Tecnologia"))
    context = {"posts":posts}
    return render(request, "tecnologia.html",context)

def videojuegos(request):
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact="Videojuegos"))
    context = {"posts":posts}
    return render(request, "videojuegos.html",context)
