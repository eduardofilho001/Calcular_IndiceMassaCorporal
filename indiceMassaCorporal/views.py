from django.shortcuts import render
from .forms import FormIMC

def index(request):
    form = FormIMC()
    
    return render(request, 'index.html', {
        "form" : form
    })

def resultado(request):
    peso = None
    altura = None
    resultado = None
    
    if request.method == "POST":
        form = FormIMC(request.POST)
        if form.is_valid():
            peso = form.cleaned_data["peso"]
            altura = form.cleaned_data["altura"]
            
            resultado = peso/(altura*altura)

    return render(request, 'resultado.html', {
        "peso":peso,
        "altura":altura,
        "resultado":resultado
    })
