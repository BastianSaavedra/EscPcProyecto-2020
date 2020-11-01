from django.shortcuts import render, redirect, get_object_or_404
from . models import PlacasMadre,Procesadore,Gpu,Ram,Almacenamiento,FuentesPoder,Gabinete,Monitore
from django.views.generic import ListView, DetailView
from .forms import PlacaForm, ContactoForm, ProceForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html',)

def contacto(request):
    return render(request,'contacto.html',)

def placamadre(request):
    productoPlaca = PlacasMadre.objects.all()

    return render(
        request,
        'placasmadres.html',
        context={'productoPlaca':productoPlaca},
    )

def procesador(request):
    productoProce = Procesadore.objects.all()

    return render (
        request,
        'procesadores.html',
        context={'productoProce': productoProce},
    )

def video(request):
    productoGpu = Gpu.objects.all()

    return render (
        request,
        'tarjetadevideo.html',
        context={'productoGpu':productoGpu},
    )

def rams(request):
    productoRam = Ram.objects.all()

    return render(
        request,
        'ram.html',
        context={'productoRam':productoRam},
    )

def alma(request):
    productoAlmacenamiento = Almacenamiento.objects.all()

    return render(
        request,
        'almacenamiento.html',
        context={'productoAlmacenamiento':productoAlmacenamiento},
    )

def fuente(request):
    productoFuente = FuentesPoder.objects.all()

    return render(
        request,
        'fuenteDePoder.html',
        context={'productoFuente':productoFuente},
    )

def gabo(request):
    productoGabo = Gabinete.objects.all()

    return render(
        request,
        'gabinetes.html',
        context={'productoGabo':productoGabo},
    )

def moni(request):
    productoMoni = Monitore.objects.all()

    return render(
        request,
        'monitores.html',
        context={'productoMoni':productoMoni},
    )

#VISTAS PLACA
class PlacaListView(ListView):
    model = PlacasMadre
    template_name = 'catalogo/placasmadre_list.html'

class PlacaDetailView(DetailView):
    model = PlacasMadre
    template_name = 'catalogo/placasmadre_detail.html'

#VISTAS PROCESADOR
class ProceListView(ListView):
    model = Procesadore
    template_name = 'catalogo/procesadore_list.html'

class ProceDetailView(DetailView):
    model = Procesadore
    template_name = 'catalogo/procesadore_detail.html'

#CRUD PLACASMADRE
#AGREGAR PLACA
def nueva_placa(request):
    data = {
        'form':PlacaForm()
    }
    if request.method == 'POST':
        formulario = PlacaForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto ingresado exitosamente!")
            return redirect(to="placas")
    return render(request, 'catalogo/nueva_placa.html', data)

#MODIFICAR PLACA
def modificar_placa(request, id):
    placa = get_object_or_404(PlacasMadre, id=id)
    data = {
        'form':PlacaForm(instance=placa)
    }
    if request.method == 'POST':
        formulario = PlacaForm(data=request.POST, instance=placa, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto modificado exitosamente!")
            return redirect(to="placas")
        data["form"] = formulario
    return render(request,'catalogo/modificar_placa.html', data)

#ELIMINAR PLACA
def eliminar_placa(request, id):
    placa = get_object_or_404(PlacasMadre, id=id)
    placa.delete()
    messages.success(request, "Producto eliminado exitosamente!")
    return redirect(to="placas")

#CRUD PROCESADOR
#AGREGAR PROCESADOR
def nuevo_procesador(request):
    data = {
        'proceform':ProceForm()
    }
    if request.method == 'POST':
        formulario = ProceForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto ingresado exitosamente!")
            return redirect(to="procesadores")
    return render(request, 'catalogo/nuevo_procesador.html', data)

#MODICIAR PROCESDOR
def modicar_procesador(request, id):
    proce = get_object_or_404(Procesadore, id=id)
    data = {
        'proceform':ProceForm(instance=proce)
    }
    if request.method == 'POST':
        formulario = ProceForm(data=request.POST, instance=proce, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "producto modificado exitosamente!")
            return redirect(to="procesadores")
        data["proceform"] = formulario
    return render(request, 'catalogo/modificar_procesador.html', data)

#ELIMINAR PROCESADOR
def eliminar_procesador(request, id):
    proce = get_object_or_404(Procesadore, id=id)
    proce.delete()
    messages.success(request, "Producto eliminado exitosamente!")
    return redirect(to="procesadores")

#CONTACTO
def contacto(request):
    data = {
        'contactoform':ContactoForm()
    }
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensaje enviado exitosamente!")
        else:
            data["contactoform"] = formulario
    return render(request, 'contacto.html', data)
