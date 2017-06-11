import os
from contextlib import contextmanager

import click

from pet import bl
from pet.exceptions import Info, PetException

cli = click.Group()
active_project = os.environ.get('PET_ACTIVE_PROJECT', '')


@contextmanager
def pet_exception_manager():
    try:
        yield
    except Info as ex:
        click.secho(ex.__class__.__name__ + ": " + ex.__str__(), fg='magenta')
    except PetException as ex:
        click.secho(ex.__class__.__name__ + ": " + ex.__str__(), fg='red')


def get_projects():
    project_list = []
    with pet_exception_manager():
        bl_output = bl.print_list()
        if bl_output:
            project_list = bl_output.splitlines()
        return project_list


def get_tasks(project_name):
    task_list = []
    with pet_exception_manager():
        bl_output = bl.print_tasks(project_name)
        if bl_output:
            task_list = bl_output.splitlines()
        return task_list


class ProjectCli(click.MultiCommand):

    def list_commands(self, ctx):
        return []

    def get_command(self, ctx, name):
        def _project_cli(project_name):
            @click.command(project_name)
            @click.option('-l', is_flag=True, help="Lock project")
            def project_cli(l):
                with pet_exception_manager():
                    bl.start(project_name=project_name, lock=bool(l))

            return project_cli

        projects = get_projects()
        if name in projects:
            return _project_cli(name)


class ActiveCli(click.MultiCommand):

    def list_commands(self, ctx):
        return []

    def get_command(self, ctx, name):
        def _task_cli(project_name, task_name):
            @click.command(task_name)
            @click.argument('args', nargs=-1)
            @click.option('-i', '--interactive', is_flag=True)
            def task_cli(interactive, args=()):
                with pet_exception_manager():
                    bl.run_task(project_name, task_name, interactive, args)

            return task_cli

        tasks = get_tasks(active_project)
        if name in tasks:
            return _task_cli(active_project, name)


@cli.command('init')
@click.option('--name', '-n', default=None, help="name for project")
@click.option('--in_place', '-i', is_flag=True, help="saves project files in ./.pet/")
@click.option('--templates', '-t', multiple=True, help="-t template,template... or -t template -t template")
def create_project(name, in_place, templates):
    """creates new project"""
    if not name:
        name = os.path.basename(os.getcwd())
    if len(templates) == 1:
        if templates[0].count(',') > 0:
            templates = templates[0].split(',')
    with pet_exception_manager():
        bl.create(name, in_place, templates)


@cli.command('list')
@click.option('--active', '-a', is_flag=True, help="print active projects")
@click.option('--old', '-o', is_flag=True, help="print projects in archive")
@click.option('--tasks', '-t', is_flag=True, help="show tasks in active project")
@click.option('--tree', is_flag=True, help="show tree of all tasks in projects")
@click.option('--templates', is_flag=True, help="show all available template")
def print_list(active, old, tasks, tree, templates):
    """lists all projects/ archived projects/ tasks/ all"""
    with pet_exception_manager():
        if [active, old, tree, tasks, templates].count(True) > 1:
            click.secho("Only one flag at a time! I am not Mt Everest", fg='red')
            return 1
        if old:
            projects = bl.print_old()
            if projects:
                click.echo(projects)
        elif tasks:
            if active_project:
                tasks_list = bl.print_tasks(active_project)
                if tasks_list:
                    click.echo(tasks_list)
            else:
                click.secho("No project activated", fg='red')
        elif tree:
            tree = bl.print_tree()
            if tree:
                click.echo(tree)
        elif templates:
            templates = bl.print_templates()
            if templates:
                click.echo(templates)
        elif active:
            active_list = bl.print_active()
            if active_list:
                click.echo(active_list)
        else:
            projects = bl.print_list()
            if projects:
                click.echo(projects)


@cli.command('archive')
@click.option('-t', '--template', is_flag=True, help="copy project to templates")
@click.argument('project_name')
def archive(project_name, template):
    """archives project or adds it to templates"""
    with pet_exception_manager():
        if template:
            bl.add_to_templates(project_name=project_name)
        else:
            bl.archive(project_name=project_name)


@cli.group()
def config():
    """configures pet"""
    pass


@config.command()
def shell():
    """helps you edit shell_profiles file"""
    with pet_exception_manager():
        bl.edit_shell_profiles()


@config.command()
def projects_folder():
    """helps you add PET_FOLDER variable"""
    with pet_exception_manager():
        click.secho("Current folder used for pet files is:\n{0}".format(bl.get_pet_folder()), fg='green')
    click.secho("You can change folder that is going to be recognized by pet, by adding\n"
                "export PET_FOLDER='path'\nto your shell profile file", fg='green')


@config.command()
def editor():
    """helps you change editor used in pet actions"""
    with pet_exception_manager():
        bl.edit_config()


@cli.command()
@click.argument('project_name')
def restore(project_name):
    """restores project from archive"""
    with pet_exception_manager():
        bl.restore(project_name)


@cli.command()
@click.option('--name', '-n', default="", help="name for project")
def register(name):
    """registers .pet as project folder"""
    if not name:
        name = os.path.basename(os.getcwd())
    with pet_exception_manager():
        bl.register(project_name=name)


@cli.command()
@click.argument('project_name')
@click.argument('task_name')
@click.option('-i', '--interactive', is_flag=True)
@click.argument('args', nargs=-1)
def run(project_name, task_name, interactive, args=()):
    """runs projects task"""
    with pet_exception_manager():
        bl.run_task(
            project_name=project_name, task_name=task_name, interactive=interactive, args=args)


@cli.command()
def recreate():
    """Recreates all required folders in PET_FOLDER"""
    with pet_exception_manager():
        bl.recreate()


@cli.command()
@click.option('-s', '--shell_type', default=os.environ.get('SHELL', ''))
def deploy(shell_type):
    """Deploys auto-completion"""
    with pet_exception_manager():
        bl.deploy(shell_type)


if active_project:
    @cli.command()
    @click.option('-s', '--save', 'how', flag_value='save', help="save as normal task")
    @click.option('-l', '--local', 'how', flag_value='local', help="save as local task")
    @click.option('-a', '--no_alias', is_flag=True, help="don't add alias [task_name]=...")
    @click.argument('task_name', metavar='TASK_NAME[.<extension>]')
    def task(task_name, no_alias, how):
        """creates new task"""
        if how:
            with pet_exception_manager():
                bl.create_task(active_project, task_name, no_alias, how)
        else:
            click.secho("Choose either --save to save as normal task\n"
                        "either --local to save as local task", fg="magenta")

    @cli.command()
    def stop():
        """stops project"""
        with pet_exception_manager():
            bl.stop()

    @cli.command('remove')
    @click.option('-l', '--locks', is_flag=True, help="unlocks all projects")
    @click.argument('task_name', nargs=-1)
    @click.pass_context
    def remove_task(ctx, locks, task_name):
        """removes task or locks"""
        with pet_exception_manager():
            if locks:
                bl.clean()
            elif task_name:
                bl.remove_task(active_project, task_name[0])
            else:
                click.secho(ctx.invoke(lambda: remove_task.get_help(ctx)))

    @cli.command('rename')
    @click.argument('old_task_name')
    @click.argument('new_task_name')
    def rename_task(old_task_name, new_task_name):
        """renames task"""
        with pet_exception_manager():
            bl.rename_task(active_project, old_task_name, new_task_name)

    @cli.command()
    @click.option('-l', '--local', is_flag=True)
    @click.argument('task_name', nargs=-1)
    def edit(task_name, local):
        """edits task if given name else active project"""
        with pet_exception_manager():
            if len(task_name) > 0:
                if local:
                    bl.edit_task_locals(active_project, task_name[0])
                else:
                    bl.edit_task(active_project, task_name[0])
            else:
                if local:
                    bl.edit_project_locals(active_project)
                else:
                    bl.edit_project(active_project)
else:
    @cli.command('remove')
    @click.option('-l', '--locks', is_flag=True, help="unlocks all projects")
    @click.argument('project_name', nargs=-1)
    @click.pass_context
    def remove_project(ctx, locks, project_name):
        """removes project or locks"""
        with pet_exception_manager():
            if locks:
                bl.clean()
            elif project_name:
                bl.remove_project(project_name=project_name[0])
            else:
                click.secho(ctx.invoke(lambda: remove_project.get_help(ctx)))

    @cli.command('rename')
    @click.argument('old_project_name')
    @click.argument('new_project_name')
    def rename_project(old_project_name, new_project_name):
        """renames project"""
        with pet_exception_manager():
            bl.rename_project(old_project_name, new_project_name)

    @cli.command()
    @click.option('-l', '--local', is_flag=True)
    @click.argument('project_name')
    def edit(project_name, local):
        """edits project"""
        with pet_exception_manager():
            if local:
                bl.edit_project_locals(project_name)
            else:
                bl.edit_project(project_name)


def main():
    if active_project:
        active_cli = ActiveCli()
    else:
        active_cli = click.Group()
    projects_cli = ProjectCli()

    @click.command(
        cls=click.CommandCollection,
        sources=[cli, active_cli, projects_cli],
        invoke_without_command=True
    )
    @click.option('--version', '-v', help="show program's version number and exit", is_flag=True)
    @click.pass_context
    def multi_cli(ctx, version):
        if version:
            from pet import version
            newest_version = bl.check_version()
            if version != newest_version:
                click.secho('New pet version available. Using: {0}, available: {1}'.format(
                    version, newest_version), fg='red')
            else:
                click.secho("pet version {0}".format(version))
        elif not ctx.invoked_subcommand:
            click.secho(ctx.invoke(lambda: multi_cli.get_help(ctx)))

    multi_cli()

if __name__ == '__main__':
    main()
