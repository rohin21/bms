import graphene

class Login(graphene.ObjectType):
    login_id = graphene.UUID()
    login_role_id = graphene.UUID()
    login_username = graphene.String()
    user_password = graphene.String()
