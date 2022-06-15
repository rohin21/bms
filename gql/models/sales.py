import graphene

class Sales(graphene.ObjectType):
    sale_id = graphene.UUID()
    sale_cus_id = graphene.UUID()
    sale_amt = graphene.String()
    sale_desc = graphene.String()
    sale_type = graphene.String()