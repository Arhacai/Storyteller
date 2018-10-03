from django.shortcuts import render, get_object_or_404

from .models import Story


def homepage(request):
    prologue = Story.objects.get_or_create(
        title='Prologo',
        text='Debes editar este prologo.'
    )
    stories = Story.objects.exclude(title=prologue.title)
    return render(
        request, 'index.html', {'prologue': prologue, 'stories': stories}
    )


def story_detail(request, pk):
    story = get_object_or_404(Story, pk=pk)
    return render(request, 'story/story_detail.html', {'story': story})