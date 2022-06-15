import graphene

class Book(graphene.ObjectType):
    book_id = graphene.UUID()
    book_name = graphene.String()
    book_desc = graphene.String()
    book_type = graphene.String()
    book_author = graphene.String()
    book_price = graphene.Int()
