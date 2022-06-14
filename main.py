import graphene
from fastapi import FastAPI
from starlette_graphene3 import GraphQLApp, make_playground_handler
from starlette.applications import Starlette
from gql import Query

app = FastAPI()

@app.get('/')
def index():
    return "Hello"

star_gql = Starlette()

schema = graphene.Schema(query=Query)
app.mount("/gql", GraphQLApp(schema, on_get=make_playground_handler()))