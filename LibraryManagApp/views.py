from django.shortcuts import render
from . models import *
from . forms import *
from django.http import HttpResponse
import requests
from datetime import datetime

from django.contrib import messages
# Create your views here.
from django.db.models import Q

def save_data_to_database(books):
    print(books)
    for book_data in books["message"]:
        input_date = datetime.strptime(book_data['publication_date'], "%m/%d/%Y")
        book = Books(
            bookID=book_data['bookID'],
            title=book_data['title'],
            authors=book_data['authors'],
            average_rating=book_data['average_rating'],
            isbn=book_data['isbn'],
            isbn13=book_data['isbn13'],
            language_code=book_data['language_code'],
            ratings_count=book_data['ratings_count'],
            text_reviews_count=book_data['text_reviews_count'],
            publication_date=input_date,
            publisher=book_data['publisher']
        )
        book.save()


def index(request):
    return render(request,"index.html")


def adminlogin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = AdminLogin.objects.filter(username=username,password=password)
        if user.exists():
            if Books.objects.exists():
                pass
            else:
                api_url = "https://frappe.io/api/method/frappe-library?page=2&title=and"
                response = requests.get(api_url)
                data = response.json()
                save_data_to_database(data)
            return render(request,"adminhome.html",{"books": Books.objects.all()})
        else:
            return render(request,"adminlogin.html")
    else:
        return render(request,"adminlogin.html")
    
def editbook(request,pk):
    book = Books.objects.get(id=pk)
    if request.method == "POST":
        # book.publication_date = datetime.strptime(request.POST["publication_date"], "%m/%d/%Y")
        book.title = request.POST["title"]
        book.authors = request.POST["authors"]
        book.language_code = request.POST["language_code"]
        book.publication_date = request.POST["publication_date"]
        book.publisher = request.POST["publisher"]
        book.save()
        return render(request,"adminhome.html",{"books": Books.objects.all()})
    else:
        return render(request,"edit.html",{"book":book})
    
def delete(request,pk):
    book = Books.objects.filter(id=pk)
    book.delete()
    return render(request,"adminhome.html",{"books": Books.objects.all()})


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if Registrations.objects.filter(email=request.POST["email"]):
            messages.success(request,"Email is already registered...")
            return render(request,"index.html")
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successful...")
            return render(request,"index.html")
        else:
            print("invalid")    
    else:
        return render(request,"registration.html")


def userlogin(request):
    user = Registrations.objects.filter(email=request.POST['email'],
                                        password=request.POST['password'],
                                        )
    if user.exists():
        if Books.objects.exists():
            return render(request,"userhome.html",{"books": Books.objects.all(),
                                            "email":request.POST['email'],
                                            "rbooks":RentedBooks.objects.filter(user_email=request.POST['email'])})
        else:
            api_url = "https://frappe.io/api/method/frappe-library?page=2&title=and"
            response = requests.get(api_url)
            data = response.json()
            save_data_to_database(data)
            return render(request,"userhome.html",{"books": Books.objects.all(),
                                                "email":request.POST['email'],
                                                "rbooks":RentedBooks.objects.filter(user_email=request.POST['email'])})
    else:
        messages.error(request,"invalid Credentials...")
        return render(request,"index.html")


def searchbook(request):
    if request.method == "POST":
        name = request.POST['name']
        # Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias'))
        try:
            book = Books.objects.get(Q(title=name) | Q(authors=name))
            return render(request,"singlebookadmin.html",{"book":book})
        except:
            messages.error(request,"Currently Book is not available...")
            return render(request,"adminhome.html",{"books": Books.objects.all()})
            
    else:
        return render(request,"searchbook.html")
    

def bookissue(request,pk,email):
    if RentedBooks.objects.filter(user_email=email):
        messages.error(request,"You already have one library book.Please pay any previous fees then you can issue a new book")
        return render(request,"userhome.html",{"books": Books.objects.all(),
                                               "email":email,
                                               "rbooks":RentedBooks.objects.filter(user_email=email)})
    else:    
        book = Books.objects.get(id=pk)
        print(book.id,book.title)
        issuedbook = RentedBooks(user_email=email,
                                book_id=book.id,
                                title=book.title,
                                authors=book.authors,
                                publisher=book.publisher)
        issuedbook.save()
        messages.success(request,"Book issued...")
        return render(request,"userhome.html",{"books": Books.objects.all(),"email":email,
                                            "rbooks":RentedBooks.objects.filter(user_email=email)})

def deleteissuedbook(request,pk):
    book = RentedBooks.objects.get(id=pk)
    book.delete()
    return render(request,"issuebooks.html",{"books":RentedBooks.objects.all()})

def issuedbooks(request):
    return render(request,"issuebooks.html",{"books":RentedBooks.objects.all()})

def addbook(request):
    if request.method == "POST":
        form = BooksForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"adminhome.html",{"books": Books.objects.all()})
        else:
            return HttpResponse("Error")
    return render(request,"addbook.html")

def payfees(request,email):
    book = RentedBooks.objects.filter(user_email=email)
    book.delete()
    return render(request,"userhome.html",{"books": Books.objects.all(),"email":email,
                                            "rbooks":RentedBooks.objects.filter(user_email=email)})

def recoverbooks(request):
    ids = []
    books = Books.objects.all()
    for i in books:
        ids.append(i.bookID)
    api_url = "https://frappe.io/api/method/frappe-library?page=2&title=and"
    response = requests.get(api_url)
    data = response.json()    
    for book_data in data["message"]:
        if book_data['bookID'] not in ids:
            input_date = datetime.strptime(book_data['publication_date'], "%m/%d/%Y")
            book = Books(
                bookID=book_data['bookID'],
                title=book_data['title'],
                authors=book_data['authors'],
                average_rating=book_data['average_rating'],
                isbn=book_data['isbn'],
                isbn13=book_data['isbn13'],
                language_code=book_data['language_code'],
                ratings_count=book_data['ratings_count'],
                text_reviews_count=book_data['text_reviews_count'],
                publication_date=input_date,
                publisher=book_data['publisher']
            )
            book.save()
    messages.success(request,"Books Recovered....")
    return render(request,"adminhome.html",{"books": Books.objects.all()})
