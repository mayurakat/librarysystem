from users import views
from django.urls import path

urlpatterns = [
    path('home/',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('books/',views.books,name='books'),
    path('users/',views.users,name='users'),
    path('delbook/<int:pk>/',views.delete_book,name='delbook'),
]