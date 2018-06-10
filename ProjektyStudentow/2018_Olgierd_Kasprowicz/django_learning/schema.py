import graphene
import sample_app.schema


class Query(sample_app.schema.Query, graphene.ObjectType):
    pass


class MyMutations(graphene.ObjectType):
    create_machine = sample_app.schema.CreateMachine.Field()
    create_command = sample_app.schema.CreateCommand.Field()


schema = graphene.Schema(query=Query, mutation=MyMutations)
