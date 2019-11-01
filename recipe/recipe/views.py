from django.shortcuts import render, HttpResponseRedirect, reverse
from django.utils import timezone
from recipe.models import Recipe, Author, Recipe
from recipe.forms import AuthorAdd, RecipeAdd



def index(request):
    html = "index.html"

    news = Recipe.objects.all()

    return render(request, html, {'data': news})

def author_view(request,id):
    html = "author.html"

    auth = Author.objects.filter(id=id)

    recipes = Recipe.objects.filter(author=auth.first())

    return render(request,html,{"auth":auth,"recipes":recipes})

def recipe_view(request,id):
    html = "recipe.html"

    reci = Recipe.objects.filter(id=id)

    return render(request,html,{"reci":reci})

def author_form_view(request):
    html = 'genericform.html'

    if request.method == 'POST':
        form = AuthorAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(
                name=data['name'],
                bio=data['bio']
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = AuthorAdd()

    return render(request, html, {'form':form})

def recipe_form_view(request):
    html = 'genericform.html'

    if request.method == 'POST':
        form = RecipeAdd(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title=data['title'],
                author=data['author'],
                description=data['description'],
                instructions=data['instructions'],
                reqtime=data['reqtime'],
                post_date=timezone.now()
            )
            return HttpResponseRedirect(reverse('homepage'))
    form = RecipeAdd()

    return render(request, html,{'form': form})
