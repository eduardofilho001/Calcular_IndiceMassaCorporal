from django.shortcuts import render

def index(request):    
    return render(request, 'index.html')

def resultado(request):

    peso = float(input(request.POST.get('peso')))
    altura = float(input(request.POST.get('altura')))

    resultado = peso / (altura * altura)
    
    return render(request, 'resultado.html', {
        "resultado" : resultado
    })
