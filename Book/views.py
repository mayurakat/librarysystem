from django.shortcuts import render
from .models import Book
from .resources import BookResource
from tablib import Dataset
from django.contrib import messages

# Create your views here.
def upload_file(request):
    if request.method == "POST":
        book_resource = BookResource()
        dataset = Dataset()
        file = request.FILES['File']

        if not file.name.endswith('xlsx'):
            messages.info(request,"wrong file format")
            return render(request,'add_book.html')
        file_data = dataset.load(file.read(),format='xlsx')
        for data in file_data:
            value = Book(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4]
            )
            value.save()
    return render(request,'add_book.html')       