from django.shortcuts import render


from .models import Post


def index(request):
    posts = Post.objects.all
    return render(request, 'videogame_app/index.html', {'posts': posts})








