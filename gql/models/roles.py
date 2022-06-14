import graphene

class Role(graphene.ObjectType):
    role_id = graphene.UUID()
    role_name = graphene.String()
    role_desc = graphene.String()