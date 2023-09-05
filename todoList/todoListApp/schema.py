import graphene
from graphene_django import DjangoObjectType
from todoListApp.models import Todo
from graphql_auth.schema import UserQuery,MeQuery
from graphql_auth import mutations

class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description', 'time')

class Query(graphene.ObjectType):
    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        return Todo.objects.all()

class CreateTodoMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        time = graphene.String(required=True)

    todo = graphene.Field(TodoType)

    def mutate(self, info, title, description, time):
        todo = Todo.objects.create(title=title, description=description, time=time)
        return CreateTodoMutation(todo=todo)

class Mutation(graphene.ObjectType):
    create_todo = CreateTodoMutation.Field()

class AuthMutation(graphene.ObjectType):
    register=mutations.Register.Field()
    token_auth=mutations.ObtainJSONWebToken.Field()

class Query(UserQuery,MeQuery,graphene.ObjectType):
    pass

class Mutation(AuthMutation,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query,mutation=Mutation)