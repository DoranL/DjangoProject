from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import App, Rank
from django.http import HttpResponse, JsonResponse

from steam import Steam
from decouple import config
import json

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


# Create your views here.
class IndexView(generic.ListView):
    model = App
    template_name = "index.html"


class SearchView(generic.ListView):
    model = App
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = App.objects.filter(
            Q(name__icontains=query) | Q(id__icontains=query)
        )
        return object_list


class DetailView(generic.TemplateView):
    template_name = "detail.html"
    # 데이터 불러오기
    def get(self, request, pk, **kwargs):
        context = super().get_context_data(**kwargs)
        user = steam.apps.get_app_details(pk)
        try:
            context = {
                'json_data': json.loads(user)[str(pk)]['data']
            }
        except:
            context = {'json_data': json.loads(user)[str(pk)]}
        return render(request, 'detail.html', context)

class HomeView(generic.ListView):
    model = Rank
    template_name = "home.html"
    context_object_name = "info_list"


class RankView(generic.ListView):
    model = Rank
    template_name = "rank.html"


class SaleView(generic.ListView):
    model = App
    template_name = 'sale.html'
