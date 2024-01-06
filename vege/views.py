from django.shortcuts import render
from django.shortcuts import redirect
from .models import *

# Create your views here.

def home(request):
    return render(request, 'home.html')

def recipes(request):

    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        recipe_description = request.POST['recipe_description']
        recipe_image = request.FILES['recipe_image']

        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )

        return redirect(request, 'recipes.html')
    
    queryset = Recipe.objects.all()

    context = {
        'recipes': queryset
    }

    return render(request, 'recipes.html', context)

def recipe_delete(request, id):
    Recipe.objects.get(id=id).delete()

    return redirect('recipes')

def recipe_update(request, id):
    recipe = Recipe.objects.get(id=id)

    if request.method == 'POST':
        recipe_name = request.POST['recipe_name']
        recipe_description = request.POST['recipe_description']
        recipe_image = request.FILES['recipe_image']

        recipe.recipe_name = recipe_name
        recipe.recipe_description = recipe_description
        recipe.recipe_image = recipe_image

        recipe.save()

        return redirect('recipes')

    context = {
        'recipe': recipe
    }

    return render(request, 'recipe_update.html', context)