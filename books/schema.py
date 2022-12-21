import graphene
from graphene_django import DjangoObjectType
from .models import Books


# describe models.
class BooksType(DjangoObjectType):
    class Meta:
        model = Books
        fields = ("id", "title", "excerpt")

class Query(graphene.ObjectType):
    # Getting all books data
    all_books = graphene.List(BooksType)

    def resolve_all_books(root, info):
        return Books.objects.all()


# Build schema.
schema = graphene.Schema(
    query=Query
)