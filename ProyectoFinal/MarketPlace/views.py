from django.shortcuts import render
from django.http import HttpResponse

from MarketPlace.models import Vehiculo
from MarketPlace.models import Categoria
from MarketPlace.models import Vendedor

from django.core import serializers

from MarketPlace.forms import VehiculoFormulario
from MarketPlace.forms import CategoriaFormulario
from MarketPlace.forms import VendedorFormulario
# Create your views here.
def inicio(request):
    return render(request, 'MarketPlace/inicio.html')

def vehiculos(request):
    if request.method == "POST":
            miFormulario = VehiculoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                vehiculo = Vehiculo(marca=informacion["marca"], modelo=informacion["modelo"], año=informacion["año"]) #, kilometraje=informacion["kilometraje"]
                vehiculo.save()
                return render(request, 'MarketPlace/vehiculos.html')
    else:
        miFormulario = VehiculoFormulario()
    
    return render(request, 'MarketPlace/vehiculos.html',{"miFormulario":miFormulario})

def categorias(request):
    if request.method == "POST":
            miFormulario = CategoriaFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                categoria = Categoria(tipo_vehiculo=informacion["tipo_vehiculo"], combustible=informacion["combustible"], cilindrada_motor=informacion["cilindrada_motor"])
                categoria.save()
                return render(request, 'MarketPlace/inicio.html')
    else:
        miFormulario = CategoriaFormulario()
    return render(request, 'MarketPlace/categorias.html',{"miFormulario":miFormulario})

def vendedores(request):
    if request.method == "POST":
            miFormulario = VendedorFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
        
            if miFormulario.is_valid:
                informacion = miFormulario.cleaned_data
                vendedor = Vendedor(nombre=informacion["nombre"], telefono=informacion["telefono"], correo=informacion["correo"])
                vendedor.save()
                return render(request, 'MarketPlace/inicio.html')
    else:
        miFormulario = VendedorFormulario()
    return render(request, 'MarketPlace/vendedores.html',{"miFormulario":miFormulario})

def vehiculosapi(request):
    vehiculos_todos = Vehiculo.objects.all()
    return HttpResponse(serializers.serialize('json',vehiculos_todos))

def categoriasapi(request):
    categorias_todas = Categoria.objects.all()
    return HttpResponse(serializers.serialize('json',categorias_todas))

def vendedoresapi(request):
    vendedores_todos = Vendedor.objects.all()
    return HttpResponse(serializers.serialize('json',vendedores_todos))

#Buscar Vehiculos
def buscar(request):
    marca_views = request.GET['marca']
    vehiculos_todos = Vehiculo.objects.filter(marca=marca_views)
    return render(request, 'MarketPlace/resultadoVehiculos.html',{'marca':marca_views,'vehiculos':vehiculos_todos})

def buscarvehiculo(request):
    return render(request, 'MarketPlace/busquedaVehiculos.html')

#Buscar Vendedores
def buscarv(request):
    nombre_views = request.GET['nombre']
    vendedores_todos = Vendedor.objects.filter(nombre=nombre_views)
    return render(request, 'MarketPlace/resultadoVendedores.html',{'nombre':nombre_views,'vendedores':vendedores_todos})

def buscarvendedor(request):
    return render(request, 'MarketPlace/busquedaVendedores.html')

#Buscar Categorias
def buscarc(request):
    tipo_vehiculo_views = request.GET['tipo_vehiculo']
    categorias_todas = Categoria.objects.filter(tipo_vehiculo=tipo_vehiculo_views)
    return render(request, 'MarketPlace/resultadoCategorias.html',{'tipo_vehiculo':tipo_vehiculo_views,'categorias':categorias_todas})

def buscarcategoria(request):
    return render(request, 'MarketPlace/busquedaCategorias.html')

#Create Read Update Delete

#Vehiculos

def leer_vehiculos(request):
    vehiculos_all = Vehiculo.objects.all()
    return HttpResponse(serializers.serialize ('json',vehiculos_all))

def crear_vehiculo(request):
    vehiculo = Vehiculo(marca= 'Vehiculotest' , modelo='test', año=1)
    vehiculo.save()
    return HttpResponse(f'Vehiculo {vehiculo.modelo} ha sido creado')

def editar_vehiculo(request):
    modelo_consulta = 'test'
    Vehiculo.objects.filter(modelo=modelo_consulta).update(modelo= 'ModelonuevoTest')
    return HttpResponse(f'Vehiculo {modelo_consulta} ha sido actualizado')

def eliminar_vehiculo(request):
    modelo_nuevo = 'ModelonuevoTest'
    vehiculo = Vehiculo.objects.get(modelo= modelo_nuevo)
    vehiculo.delete()
    return HttpResponse(f'Vehiculo {modelo_nuevo} ha sido eliminado')


from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#Vehiculos

class VehiculoList(ListView):
    model = Vehiculo
    template_name = 'MarketPlace/vehiculos_list.html' 

class VehiculoCreate(CreateView):
    model = Vehiculo
    fields ='__all__'
    success_url = '/MarketPlace/vehiculo/list/'

class VehiculoEdit(UpdateView):
    model = Vehiculo
    fields ='__all__'
    success_url = '/MarketPlace/vehiculo/list/'

from django.views.generic.detail import DetailView

class VehiculoDetail(DetailView):
    model = Vehiculo
    template_name = 'MarketPlace/vehiculos_detail.html'

class VehiculoDelete(DeleteView):
    model = Vehiculo
    #fields ='__all__'
    success_url = '/MarketPlace/vehiculo/list/'


#Create Read Update Delete

#Categorias

def leer_categorias(request):
    categorias_all = Categoria.objects.all()
    return HttpResponse(serializers.serialize ('json',categorias_all))

def crear_categoria(request):
    categoria = Categoria(tipo_vehiculo= 'Categoriatest' , combustible='test', cilindrada_motor=1000)
    categoria.save()
    return HttpResponse(f'Categoria {categoria.combustible} ha sido creada')

def editar_categoria(request):
    combustible_consulta = 'test'
    Categoria.objects.filter(combustible=combustible_consulta).update(combustible= 'CombustibleNuevoTest')
    return HttpResponse(f'Categoria {combustible_consulta} ha sido actualizada')

def eliminar_categoria(request):
    combustible_nuevo = 'CombustibleNuevoTest'
    categoria = Categoria.objects.get(combustible= combustible_nuevo)
    categoria.delete()
    return HttpResponse(f'Categoria {combustible_nuevo} ha sido eliminada')


from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#Categorias

class CategoriaList(ListView):
    model = Categoria
    template_name = 'MarketPlace/categorias_list.html' 

class CategoriaCreate(CreateView):
    model = Categoria
    fields ='__all__'
    success_url = '/MarketPlace/categoria/listC/'

class CategoriaEdit(UpdateView):
    model = Categoria
    fields ='__all__'
    success_url = '/MarketPlace/categoria/listC/'

from django.views.generic.detail import DetailView

class CategoriaDetail(DetailView):
    model = Categoria
    template_name = 'MarketPlace/categorias_detail.html'

class CategoriaDelete(DeleteView):
    model = Categoria
    #fields ='__all__'
    success_url = '/MarketPlace/categoria/listC/'


#Create Read Update Delete

#Vendedores

def leer_vendedores(request):
    vendedores_all = Vendedor.objects.all()
    return HttpResponse(serializers.serialize ('json',vendedores_all))

def crear_vendedor(request):
    vendedor = Vendedor(nombre= 'Vendedortest' , telefono=1234, correo='test@test.com')
    vendedor.save()
    return HttpResponse(f'Vendedor {vendedor.nombre} ha sido creado')

def editar_vendedor(request):
    nombre_consulta = 'test'
    Vendedor.objects.filter(nombre=nombre_consulta).update(nombre= 'NombreNuevoTest')
    return HttpResponse(f'Vendedor {nombre_consulta} ha sido actualizado')

def eliminar_vendedor(request):
    nombre_nuevo = 'NombreNuevoTest'
    vendedor = Vendedor.objects.get(nombre= nombre_nuevo)
    vendedor.delete()
    return HttpResponse(f'Vendedor {nombre_nuevo} ha sido eliminado')

from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

#Vendedores

class VendedorList(ListView):
    model = Vendedor
    template_name = 'MarketPlace/vendedores_list.html' 

class VendedorCreate(CreateView):
    model = Vendedor
    fields ='__all__'
    success_url = '/MarketPlace/vendedor/listV/'

class VendedorEdit(UpdateView):
    model = Vendedor
    fields ='__all__'
    success_url = '/MarketPlace/vendedor/listV/'

from django.views.generic.detail import DetailView

class VendedorDetail(DetailView):
    model = Vendedor
    template_name = 'MarketPlace/vendedores_detail.html'

class VendedorDelete(DeleteView):
    model = Vendedor
    #fields ='__all__'
    success_url = '/MarketPlace/vendedor/listV/'