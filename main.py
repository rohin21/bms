import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler
from starlette.applications import Starlette

app = FastAPI()

@app.get('/')
def index():
    return "Hello"

star_gql = Starlette()

class User(graphene.ObjectType):
    id = graphene.ID()
    name = graphene.String()

class Query(graphene.ObjectType):
    me = graphene.Field(User)

    def resolve_me(root, info):
        return {"id": "john", "name": "John"}

schema = graphene.Schema(query=Query)
app.mount("/gql", GraphQLApp(schema, on_get=make_playground_handler()))