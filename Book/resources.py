from pyexpat import model
from import_export import resources
from Book.models import Book


class BookResource(resources.ModelResource):
    class meta:
        model = Book
