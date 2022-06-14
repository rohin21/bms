import graphene

class Permission(graphene.ObjectType):
    permission_id = graphene.UUID()
    permission_role_id = graphene.UUID()
    permission_module = graphene.String()
    permission_name = graphene.String()
