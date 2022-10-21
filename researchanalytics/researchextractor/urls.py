from django.urls import path
from . import views

urlpatterns = [
    path('', views.getIndexView, name="index"),
    path('authors/', views.getAuthors, name="authors"),
    path('new_author/', views.createNewAuthor,name="new_authors"),
    path('new_author/add/', views.addNewAuthor,name="add_authors"),
]