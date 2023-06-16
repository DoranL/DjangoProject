import json
import requests

from django.db.models import Q
from django.shortcuts import render
from django.views import generic, View
from django.core.paginator import Paginator
from .models import App, Rank


# Create your views here.
class IndexView(View):
    def get(self, request):
        page = request.GET.get("page", 1)
        start = (page - 1) * 10
        end = page * 10
        apps = []
        for app in App.objects.all()[start:end]:
            user = requests.get(
                f"https://store.steampowered.com/api/appdetails?appids={app.id}&l=korean"
            )
            app.save()

            apps.append(user.json())

        return render(request, "index.html", {"apps": apps})


class SearchView(generic.ListView):
    model = App
    template_name = "search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = App.objects.filter(
            Q(name__icontains=query) | Q(id__icontains=query)
        )
        return object_list


class DetailView(View):
    def get(self, request, pk, **kwargs):
        context = {}
        user = requests.get(
            f"https://store.steampowered.com/api/appdetails?appids={pk}&l=korean"
        )
        data = user.json()
        try:
            context = {"json_data": data[str(pk)]["data"]}
        except:
            context = {"json_data": data[str(pk)]}
        return render(request, "detail.html", context)


class HomeView(View):
    def get(self, request):
        page = request.GET.get("page", 1)
        start = (page - 1) * 30
        end = page * 30
        apps = []
        for app in Rank.objects.all()[start:end]:
            user = requests.get(
                f"https://store.steampowered.com/api/appdetails?appids={app.app.id}&l=korean"
            )
            app.save()

            apps.append(user.json()[str(app.app.id)])

        return render(request, "home.html", {"apps": apps})


class RankView(View):
    def get(self, request):
        page = request.GET.get("page", 1)
        start = (page - 1) * 30
        end = page * 30
        apps = []
        for app in Rank.objects.all()[start:end]:
            user = requests.get(
                f"https://store.steampowered.com/api/appdetails?appids={app.app.id}&l=korean"
            )
            app.save()

            apps.append(user.json()[str(app.app.id)])

        return render(request, "rank.html", {"apps": apps})


class SaleView(generic.ListView):
    model = App
    template_name = "sale.html"
