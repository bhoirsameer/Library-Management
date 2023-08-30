from django.urls import path
from LibraryManagApp.views import *
from django.views.generic import TemplateView


urlpatterns = [

    path("",TemplateView.as_view(template_name="index.html"),name="index"),
    path("admin-login",adminlogin,name="admn-login"),
    path('edit/<int:pk>',editbook,name="edit-book"),
    path('delete/<int:pk>',delete,name="delete-book"),
    path('register',register,name="register-user"),
    path('user-login',userlogin,name="user-login"),
    path('issue-book/<int:pk>/<str:email>',bookissue,name="bookissue"),
    path('search-book',searchbook,name="search-book"),
    path('issued-books',issuedbooks,name="issued-books"),
    path('delete-issued-book/<int:pk>',deleteissuedbook,name="delete-issued-book"),
    path('addbook',addbook,name="add_book"),
    path('payfees/<str:email>',payfees,name="payfees"),
]