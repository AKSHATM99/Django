from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def recipe(request):
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        
        Recipe.objects.create(recipe_name=recipe_name,
                              recipe_image=recipe_image,
                              recipe_description=recipe_description)
        return redirect("/recipe/")
        
    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {'recipe': queryset}
    return render(request, "recipies.html", context)

def delete(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect("/recipe/")

def update(request, id):
    queryset = Recipe.objects.get(id = id)
    if request.method=="POST":
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        if recipe_name:
            queryset.recipe_name = recipe_name
        if recipe_description:
            queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("/recipe/")
    context = {'recipe': queryset}
    return render(request, "update.html", context)
