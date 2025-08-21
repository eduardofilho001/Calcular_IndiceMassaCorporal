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
    classificacao = None
    
    if request.method == "POST":
        form = FormIMC(request.POST)
        if form.is_valid():
            peso = form.cleaned_data["peso"]
            altura = form.cleaned_data["altura"]
            
            resultado = peso/(altura*altura)
    
            if resultado < 18.5: 
                classificacao = "Abaixo do Peso"

            elif 18.5 <= resultado < 25:
                classificacao="Peso Normal"

            elif 25 <= resultado < 30:
                classificacao="Sobrepeso"

            elif 30 <= resultado < 35: 
                classificacao="Obesidade Grau 1"

            elif 35 <= resultado < 40:
                classificacao="Obesidade Grau 2"

            else:
                classificacao="Obesidade Grau 3"

    return render(request, 'resultado.html', {
        "peso":peso,
        "altura":altura,
        "resultado":resultado,
        "classificacao":classificacao
    })
