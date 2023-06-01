from django.shortcuts import render

from .models import Post


def tags_render(request):
    return {
        'tags': Post.objects.values_list('tag', flat=True).distinct()
    }