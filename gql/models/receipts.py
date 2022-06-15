import graphene

class Reciepts(graphene.ObjectType):
    rec_id = graphene.UUID()
    rec_cus_id = graphene.UUID()
    rec_num = graphene.String()
    rec_desc = graphene.String()
    rec_type = graphene.String()