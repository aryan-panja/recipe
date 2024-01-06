from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist')
            return redirect('login')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, 'Username or Password is incorrect')
            return redirect('login')
        else:
            login(request, user)
            return redirect('recipes')
        
    return render(request, 'login.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username  = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()
        if user:
            messages.info(request, 'Username is already taken')
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username)
        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully')

    return render(request, 'register.html')

def logout_page(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
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

def register(request):
    return render(request, 'register.html')