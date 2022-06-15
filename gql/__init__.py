import graphene

#models
from .models.user import User
from .models.login import Login
from .models.roles import Role
from .models.permissions import Permission
from .models.receipts import Reciepts
from .models.sales import Sales
from .models.stock import Stocks
from .models.book import Book
class Query(graphene.ObjectType):
    users = graphene.Field(User)
    login = graphene.Field(Login)
    roles = graphene.Field(Role)
    permission = graphene.Field(Permission)
    books = graphene.Field(Book)
    stocks = graphene.Field(Stocks)
    reciepts = graphene.Field(Reciepts)
    sales = graphene.Field(Sales)

    def resolve_users(root, info):
        return {"id": "john", "name": "John"}