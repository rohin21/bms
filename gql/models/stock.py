import graphene

class Stocks(graphene.ObjectType):
    stk_id = graphene.UUID()
    stk_num = graphene.String()
    stk_desc = graphene.String()