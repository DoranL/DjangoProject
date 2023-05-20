from django.db.models import Q
from django.shortcuts import render
from django.views import generic

from .models import Game


# Create your views here.
class IndexView(generic.ListView):
    model = Game
    template_name = "index.html"

class SearchView(generic.ListView):
    model = Game
    template_name = 'search.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Game.objects.filter(
            Q(name__icontains=query) | Q(id__icontains=query)
        )
        return object_list

class DetailView(generic.DetailView):
    model = Game
    template_name = "detail.html"