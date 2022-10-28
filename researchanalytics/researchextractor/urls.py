from django.urls import path
from . import views

urlpatterns = [
    #Dashboard Url
    path('', views.getIndexView, name="index"),

    #Authors Urls Pattern
    path('authors/', views.getAuthors, name="authors"),
    path('author/',views.getAuthorsById,name="find_author"),
    path('new_author/', views.createNewAuthor,name="new_authors"),
    path('new_author/add/', views.addNewAuthor,name="add_authors"),
    path('new_author/edit/<str:author_id>',views.editAuthor,name="edit_author"),
    path('new_author/delete/<str:author_id>',views.removeAuthor,name="remove_author"),

    #Papers Urls
    path('papers/',views.getPapers, name='papers')
]