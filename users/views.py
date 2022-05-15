from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import  authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from .models import User
from Book.models import Book
# Create your views here.
def home(request):
    total_books = Book.objects.all().count()
    all_users = User.objects.all().count()

    context = {'total_books':total_books,'all_users':all_users}
   
    return render(request,"home.html",context)



def register(request):

    if request.method == 'POST':

        full_name = request.POST['full_name']
        mobile = request.POST['mobile']
        email= request.POST['email']
        address = request.POST['address']
        password= request.POST['password']

        if User.objects.filter(mobile = mobile).exists():
                messages.info(request, "mobile taken")
                return redirect('register')
                
        elif User.objects.filter(email = email).exists():

            messages.info(request,"email taken")
            return redirect('register')

        else:
            user = User.objects.create_user( mobile=mobile,address=address, email= email, password = password, name = full_name )
            print("user Created")
            messages.info(request, "user Created")
            return redirect('home')
    else:
        return render(request, 'register.html')



def login(request):


    if request.method == 'POST':


        email = request.POST.get('email')
        password = request.POST.get('password')        

        user = authenticate(request,email=email,password=password)

        if user:

                
            auth_login(request,user)
            messages.info(request,'You are logged in')
            return redirect('home')
        else:

            messages.info(request,'invalid user and password')
            return redirect('login')
       
    else:

        return render(request,"login.html")

def logout(request):

    auth_logout(request)
    messages.info(request,'succesfully logout')
    return redirect(login)

def books(request):
    books = Book.objects.all()
    return render(request,"books.html",{'books':books})

def users(request):
    users = User.objects.all()
    return render(request,"users.html",{'users':users})

def delete_book(request,pk):
    query = Book.objects.get(pk=pk)
    query.delete()
    messages.info(request,'book deleted')
    return redirect(home)
