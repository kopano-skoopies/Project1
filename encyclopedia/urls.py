from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>/", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("newpage/", views.newPage, name="newPage"),
    path("editpage/<str:title>/", views.editPage, name="editPage"),
    path("randompage/", views.randomPage, name="randomPage")
]
