from django.db.models import Q
from django.shortcuts import render
from django.views import generic
from .models import Info, GameName
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


class HomeView(generic.ListView):
    model = Info
    template_name = "home.html"
    context_object_name = "info_list"


class RankView(generic.ListView):
    model = Info
    template_name = "rank.html"


class SaleView(generic.ListView):
    model = Info
    template_name = 'sale.html'
