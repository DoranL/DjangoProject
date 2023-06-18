import json
import traceback
import requests

from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.core.paginator import Paginator
from .models import App, Rank


# Create your views here.
class IndexView(View):
    def get(self, request):
        page = self.request.GET.get("page", 1)
        paginator = Paginator(App.objects.all(), 10)
        page_obj = paginator.get_page(page)
        for app in page_obj:
            if app.type is None:
                user = requests.get(
                    f"https://store.steampowered.com/api/appdetails?appids={app.id}&l=korean"
                )
                json_data = user.json()[str(app.id)]
                if json_data['success']:
                    try:
                        app.initial_price = int(str(json_data['data']['price_overview']["initial"])[:-2])
                        app.discount_percent = json_data['data']['price_overview']["discount_percent"]
                        app.final_price = int(str(json_data['data']['price_overview']["final"])[:-2])
                    except:
                        traceback.format_exc()
                    finally:
                        app.type = json_data['data']["type"]
                        app.short_description = json_data['data']["short_description"]
                        app.header_image = json_data['data']["header_image"]
                        app.capsule_image = json_data['data']["capsule_image"]
                        app.is_free = json_data['data']["is_free"]
                        app.save()
        context = {'page_obj': page_obj}

        return render(request, "index.html", context)


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
        start = (page - 1) * 10
        end = page * 10
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
