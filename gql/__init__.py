import graphene

#models
from .models.user import User
from .models.login import Login
from .models.roles import Role
from .models.permissions import Permission
class Query(graphene.ObjectType):
    users = graphene.Field(User)
    login = graphene.Field(Login)
    roles = graphene.Field(Role)
    permission = graphene.Field(Permission)

    def resolve_users(root, info):
        return {"id": "john", "name": "John"}