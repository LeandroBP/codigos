from django.shortcuts import render


# HTTP REQUEST
def home(request):
    return render(request, 'recipes/pages/home.html', context={
        'name': 'Leandro Batista',  # HTTP RESPONSE
    })


def recipe(request, id):
    return render(request, 'recipes/pages/recipe-view.html')
