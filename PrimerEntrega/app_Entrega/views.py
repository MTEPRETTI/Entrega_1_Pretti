from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from app_Entrega.models import Agencia,Vendedor,Autos
from app_Entrega.forms import AppFormularios

# Create your views here.

# Create your views here.
def inicio(self):

    return render(self,'Inicio.html')

def autos(self):

    return render(self,'autos.html')


def ag3ncias(self):

    return render(self,'agencias.html')


def vendedores(self):

    return render(self,'vendedores.html')


def formularioAgencia(request):

    print('method:', request.method)
    print('post:', request.POST)
    
    if request.method == 'POST':

        miFormulario = AppFormularios(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            
            agencias = Agencia(rsoc=data['rsoc'], zona=data['zona'])
            vendedores = Vendedor(nombre=data['nombre'], apellido=data['apellido'])
            autoss = Autos(marca=data['marca'], modelo=data['modelo'])

            agencias.save()
            vendedores.save()
            autoss.save()

            return render(request, 'inicio.html')
    else:
        
        miFormulario = AppFormularios()


    return render(request,'formagen.html', {'miFormulario':miFormulario})


def busquedaAgencia(request):

    return render(request,'busquedaAgencia.html')


def buscar(request):

    if request.GET["rsoc"]:

        rsoc = request.GET["rsoc"]

        ags = Agencia.objects.filter(rsoc__icontains=rsoc)

        return render(request, "resultBusq.html", {"ags": ags, "rsoc":rsoc})
    
    else:

        respuesta = 'No enviaste datos'

    return HttpResponse(respuesta)