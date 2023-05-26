from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("rank/", views.RankView.as_view(), name="rank"),
    path("sale/", views.SaleView.as_view(), name="sale"),
    path("index/", views.IndexView.as_view(), name="index"),
    path("search/", views.SearchView.as_view(), name="search"),
    path("app/<int:pk>/", views.DetailView.as_view(), name="detail"),
]
