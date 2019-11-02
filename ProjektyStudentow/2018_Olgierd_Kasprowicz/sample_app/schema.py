import graphene
from graphene_django.types import DjangoObjectType

from sample_app.models import Command, Machine, MachineType


class CommandGraphType(DjangoObjectType):
    class Meta:
        model = Command


class MachineGraphType(DjangoObjectType):
    state = graphene.Field(CommandGraphType)

    class Meta:
        model = Machine

    def resolve_state(self, info, **kwargs):
        return self.state


class MachineTypeGraphType(DjangoObjectType):
    class Meta:
        model = MachineType


class Query(object):
    all_commands = graphene.List(CommandGraphType)
    all_machines = graphene.List(MachineGraphType)
    all_machine_types = graphene.List(MachineTypeGraphType)
    command = graphene.Field(CommandGraphType, id=graphene.Int())
    machine = graphene.Field(MachineGraphType, id=graphene.Int())
    machine_type = graphene.List(MachineTypeGraphType, id=graphene.Int(), cpu_count=graphene.Int())

    def resolve_command(self, info, **kwargs):
        id = kwargs.get('id')

        return Command.objects.get(pk=id) if id is not None else None


    def resolve_machine(self, info, **kwargs):
        id = kwargs.get('id')

        return Machine.objects.get(pk=id) if id is not None else None

    def resolve_machine_type(self, info, **kwargs):
        id = kwargs.get('id')
        cpu_count = kwargs.get('cpu_count')

        if id:
            # this must be an iterable
            return MachineType.objects.get(pk=id),
        elif cpu_count:
            return MachineType.objects.filter(cpu_count__exact=cpu_count)
        else:
            return None

    def resolve_all_commands(self, info, **kwargs):
        return Command.objects.all()

    def resolve_all_machines(self, info, **kwargs):
        return Machine.objects.all()

    def resolve_all_machine_types(self, info, **kwargs):
        return MachineType.objects.all()


class CreateMachine(graphene.Mutation):
    class Arguments:
        cpu_count = graphene.Int()
        gpu_count = graphene.Int()
        memory = graphene.Int()
        disk_space = graphene.Int()
        slug = graphene.String()

    machine_type = graphene.Field(MachineTypeGraphType)

    def mutate(self, info, **parameters):
        machine_type = MachineType(**parameters)
        machine_type.save()
        return CreateMachine(machine_type=machine_type)


class CreateCommand(graphene.Mutation):
    class Arguments:
        action = graphene.String()
        target_id = graphene.Int()

    command = graphene.Field(CommandGraphType)

    def mutate(self, info, **parameters):
        machine = Machine.objects.get(pk=parameters['target_id'])
        command = Command(action=parameters['action'], target=machine)
        current_state_command = machine.state

        if current_state_command.action == command.action:
            # no need to create another object
            return CreateCommand(command=current_state_command)
        else:
            # state changes - need to create command
            command.save()
            return CreateCommand(command=command)
