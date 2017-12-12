from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Album
# Create your views here.

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }

    return render(request, 'music/index.html', context)

def detail(request, album_id):
    """
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Can't find this album!")
    """
    album  = get_object_or_404(Album,  id=album_id)
    return render(request, 'music/detail.html', {'album': album})
