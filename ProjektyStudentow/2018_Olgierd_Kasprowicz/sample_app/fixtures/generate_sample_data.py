import json
import random
from datetime import datetime, timedelta

# in order to get deterministic results
random.seed("having fun with Django!")

reference_time = datetime.utcnow() - timedelta(1)

def n_powers_of_two(n):
    j = 1
    for i in range(n):
        yield j
        j *= 2


def generate_machine_type(id):
    return \
    {
        'model': 'sample_app.machinetype',
        'pk': id,
        'fields':
        {
            'created_at': '2018-06-09T14:07:41.865Z',
            'gpu_count': random.choice(list(n_powers_of_two(3))),
            'cpu_count': random.choice(list(n_powers_of_two(5))),
            'memory': random.choice(list(n_powers_of_two(10))),
            'disk_space': random.choice(list(n_powers_of_two(10))),
            'slug': "type-{}".format(id),
            'description': 'Lorem ipsum dolor sit amet',
        }
    }


def generate_machine(id, max_type_id):
    return \
    {
        'model': 'sample_app.machine',
        'pk': id,
        'fields':
        {
            'created_at': '2018-06-09T22:51:16.205Z',
            'type': "type-{}".format(random.randrange(max_type_id)),
            'ip': '{}.{}.{}.{}'.format(random.randrange(256), random.randrange(256), random.randrange(256), random.randrange(256)),
        }
    }


def generate_command(id, max_machine_id):
    return \
    {
        'model': 'sample_app.command', 'pk': id,
        'fields':
        {
            'created_at': (reference_time + timedelta(seconds=id)).isoformat() + 'Z',  # nifty hack to make Django shut up
            'action': random.choice(('0', '1')),
            'target': random.randrange(max_machine_id),
        }
    }


def main():
    MACHINES_TYPE_COUNT = 5
    MACHINES_COUNT = 10
    COMMANDS_COUMT = 30

    machine_types = []
    for i in range(MACHINES_TYPE_COUNT):
        machine_type = generate_machine_type(i)
        machine_types.append(machine_type)

    machines = []
    for i in range(MACHINES_COUNT):
        machine = generate_machine(i, MACHINES_TYPE_COUNT)
        machines.append(machine)

    commands = []
    for i in range(COMMANDS_COUMT):
        command = generate_command(i, MACHINES_COUNT)
        commands.append(command)

    # order matters!
    raw_output = machine_types + machines + commands

    print(json.dumps(raw_output))


if __name__ == '__main__':
    main()
