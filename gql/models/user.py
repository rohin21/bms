
import graphene

class User(graphene.ObjectType):
    user_id = graphene.UUID()
    user_name = graphene.String()
    user_mobile = graphene.String()
    user_email = graphene.String()
    user_address = graphene.String()
