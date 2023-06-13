import json
import requests

from django.db.models import Q
from django.shortcuts import render
from django.views import generic, View
from django.core.paginator import Paginator
from .models import App, Rank


# Create your views here.
class IndexView(generic.ListView):
    model = App
    template_name = "index.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        queryset = self.get_queryset()  # 모델의 쿼리셋 가져오기
        paginator = Paginator(queryset, self.paginate_by)  # Paginator 객체 생성

        page_number = self.request.GET.get("p")  # 'p'라는 이름의 페이지 번호 가져오기
        page_obj = paginator.get_page(page_number)  # 해당 페이지 객체 가져오기

        context["page_obj"] = page_obj  # 페이지 객체 컨텍스트에 추가

        return context


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
        start = (page - 1) * 10
        end = page * 10
        apps = []
        for app in App.objects.all()[start:end]:
            if app.is_free:
                apps.append({dddd})
            else:
                user = requests.get(
                    f"https://store.steampowered.com/api/appdetails?appids={app.id}&l=korean"
                )
                app.final_price = 0
                app.save()

                apps.append(user.json())

        return render(request, "home.html", {"apps": apps})


class RankView(generic.ListView):
    model = Rank
    template_name = "rank.html"


class SaleView(generic.ListView):
    model = App
    template_name = "sale.html"
