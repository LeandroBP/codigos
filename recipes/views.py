from django.http import HttpResponse
from django.shortcuts import render


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Leandro Batista',
    })
    # HTTP RESPONSE


def contato(request):
    return render(request, 'recipes/contato.html', context={
        'name': 'Python',

    })


def sobre(request):
    return HttpResponse('SOBRE')
