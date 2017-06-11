try:
    import builtins
except ImportError:
    import __builtin__
import os

import sys
import mock
import pytest

from pet.bl import (
    Bash, GeneralShellMixin, ProjectCreator, ProjectLock, Zsh, add_to_templates, archive, check_version, clean, create,
    create_task, edit_config, edit_file, edit_project, edit_shell_profiles, edit_task, get_archive_root,
    get_file_fullname, get_file_fullname_and_path, get_pet_folder, get_pet_install_folder, get_projects_root,
    get_projects_templates_root, get_shell, get_tasks_templates_root, how_many_active, lockable, print_list, print_old,
    print_projects_for_root, print_tasks, print_templates, project_exist, project_template_exist, recreate, register,
    remove_project, remove_task, rename_project, rename_task, restore, run_task, start, stop, task_exist,
    task_template_exist
)
from pet.exceptions import (
    ExceptionMessages, FolderNotFound, Info, NameAlreadyTaken, NameNotFound, PetException, ProjectActivated,
    ShellNotRecognized
)
from pet.file_templates import (
    auto_complete_zsh_deploy, edit_file_popen_template, new_project_rc_template, new_start_sh_template,
    task_exec_template
)

PET_INSTALL_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pet")
PET_FOLDER = os.environ.get('PET_FOLDER', os.path.join(os.path.expanduser("~"), ".pet/"))
projects_root = os.path.join(PET_FOLDER, "projects")
archive_root = os.path.join(PET_FOLDER, "archive")
projects_templates_root = os.path.join(PET_FOLDER, "templates", "projects")
tasks_templates_root = os.path.join(PET_FOLDER, "templates", "tasks")

if sys.version_info[0] == 2:
    builtins_name = '__builtin__'
else:
    builtins_name = 'builtins'

def lockable_t(check_only_projects=True, check_active=False):
    def _lockable_t(func, *args, **kwargs):
        def __lockable_t(self=None, project_name='', check_only=check_only_projects, *args, **kwargs):
            if self:
                return func(self, project_name, *args, **kwargs)
            else:
                return func(project_name, *args, **kwargs)
        return __lockable_t
    return _lockable_t


@mock.patch('pet.bl.glob.glob')
def test_file_fullname_command(mock_glob):
    mock_glob.return_value = ['cancer.sh']
    searching_root = "searching_here"
    file_name = "file_without_ext"
    assert get_file_fullname(searching_root, file_name) == 'cancer.sh'
    mock_glob.assert_called_with(os.path.join(searching_root, file_name + '.*'))
    mock_glob.side_effect = [None, ['bigger_cancer.sh']]
    assert get_file_fullname(searching_root, file_name) == 'bigger_cancer.sh'
    mock_glob.assert_called_with(os.path.join(searching_root, file_name))


@mock.patch('pet.bl.glob.glob')
def test_get_file_fullname_and_path(mock_glob):
    mock_glob.return_value = ['cancer.sh']
    searching_root = "searching_here"
    file_name = "file_without_ext"
    assert get_file_fullname_and_path(searching_root, file_name) == searching_root + '/cancer.sh'
    mock_glob.assert_called_with(os.path.join(searching_root, file_name + '.*'))
    mock_glob.side_effect = [None, ['bigger_cancer.sh']]
    assert get_file_fullname_and_path(searching_root, file_name) == searching_root + '/bigger_cancer.sh'
    mock_glob.assert_called_with(os.path.join(searching_root, file_name))


@mock.patch('os.path.dirname')
@mock.patch('os.path.exists')
def test_get_pet_install_folder_command(mock_exists, mock_dirname):
    mock_dirname.return_value = PET_INSTALL_FOLDER
    mock_exists.return_value = True
    assert get_pet_install_folder() == PET_INSTALL_FOLDER
    mock_exists.assert_called_with(PET_INSTALL_FOLDER)
    mock_exists.return_value = False
    with pytest.raises(FolderNotFound):
        get_pet_install_folder()


@mock.patch('os.path.expanduser')
@mock.patch('os.path.exists')
def test_get_pet_folder_command(mock_exists, mock_expand):
    mock_expand.return_value = PET_FOLDER
    mock_exists.return_value = True
    assert get_pet_folder() == PET_FOLDER
    mock_exists.assert_called_with(PET_FOLDER)
    mock_exists.return_value = False
    with pytest.raises(FolderNotFound):
        get_pet_folder()


@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.exists', return_value=True)
def test_get_projects_root_command(mock_exists, mock_get_pet_folder):
    mock_exists.return_value = True
    assert get_projects_root() == projects_root
    mock_exists.assert_called_with(projects_root)
    mock_exists.return_value = False
    with pytest.raises(FolderNotFound):
        get_projects_root()


@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.exists', return_value=True)
def test_get_projects_templates_root_command(mock_exists, mock_get_pet_folder):
    mock_exists.return_value = True
    assert get_projects_templates_root() == projects_templates_root
    mock_exists.assert_called_with(projects_templates_root)
    mock_exists.return_value = False
    with pytest.raises(FolderNotFound):
        get_projects_templates_root()


@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.exists', return_value=True)
def test_get_tasks_templates_root_command(mock_exists, mock_get_pet_folder):
    mock_exists.return_value = True
    assert get_tasks_templates_root() == tasks_templates_root
    mock_exists.assert_called_with(tasks_templates_root)
    mock_exists.return_value = False
    with pytest.raises(FolderNotFound):
        get_tasks_templates_root()


@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.exists')
def test_get_archive_root_command(mock_exists, mock_get_pet_folder):
    mock_exists.return_value = True
    assert get_archive_root() == archive_root
    mock_exists.assert_called_with(archive_root)
    mock_exists.return_value = False
    with pytest.raises(FolderNotFound):
        get_archive_root()


@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.join')
@mock.patch('pet.bl.Popen')
def test_edit_file_command(mock_popen, mock_join, mock_get_pet_folder, files):
    path = files[0]
    edit_file(path)
    mock_popen.assert_called_with([
        "/bin/sh",
        "-c",
        edit_file_popen_template.format(mock_join(), path)])


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.path.exists')
def test_project_exist_command(mock_exists, mock_projects_root, project_names):
    project_name = project_names[0]
    mock_exists.return_value = True
    assert project_exist(project_name)
    project_root = os.path.join(projects_root, project_name)
    mock_exists.assert_called_with(project_root)
    mock_exists.return_value = False
    assert not project_exist(project_name)
    mock_exists.assert_called_with(project_root)


@mock.patch('pet.bl.get_projects_templates_root', return_value=projects_templates_root)
@mock.patch('os.path.exists')
def test_template_exist_command(mock_exists, mock_templates_root, project_names):
    template_name = project_names[0]
    mock_exists.return_value = True
    assert project_template_exist(template_name)
    template_root = os.path.join(projects_templates_root, template_name)
    mock_exists.assert_called_with(template_root)
    mock_exists.return_value = False
    assert not project_template_exist(template_name)
    mock_exists.assert_called_with(template_root)


@mock.patch('pet.bl.get_tasks_templates_root', return_value=tasks_templates_root)
@mock.patch('os.path.exists')
def test_task_template_exist_command(mock_exists, mock_templates_root, task_names):
    template_name = task_names[0]
    mock_exists.return_value = True
    assert task_template_exist(template_name)
    template_root = os.path.join(tasks_templates_root, template_name)
    mock_exists.assert_called_with(template_root)
    mock_exists.return_value = False
    assert not task_template_exist(template_name)
    mock_exists.assert_called_with(template_root)


@mock.patch('pet.bl.print_tasks')
def test_task_exist_command(mock_tasks, project_names, task_names):
    project_name = project_names[0]
    task_name = task_names[0]
    mock_tasks.return_value = "{0}\ntask1\ntask2\ncov\n".format(task_name)
    assert task_exist(project_name, task_name)
    mock_tasks.assert_called_with(project_name)
    task_exist(project_name, "coverage.py")
    assert not mock_tasks.assert_called_with(project_name)


# TODO: MOCKING methods of already mocked objects
@mock.patch('pet.bl.PIPE')
@mock.patch('pet.bl.Popen')
def test_how_many_active_command(mock_popen, mock_pipe, project_names):
    process_mock = mock.Mock()
    attrs = {'stdout.read.return_value': '1\n2\n3\n'}
    process_mock.configure_mock(**attrs)
    mock_popen.return_value = process_mock
    project_name = project_names[0]
    assert how_many_active(project_name) == 3
    attrs = {'stdout.read.return_value': ''}
    process_mock.configure_mock(**attrs)
    assert how_many_active(project_name) == 0


@mock.patch('pet.bl.PIPE')
@mock.patch('pet.bl.Popen')
def test_check_version_command(mock_popen, mock_pipe):
    process_mock = mock.Mock()
    attrs = {'stdout.read.return_value': '3.4.5\n'}
    process_mock.configure_mock(**attrs)
    mock_popen.return_value = process_mock
    assert check_version() == '3.4.5'


@mock.patch('pet.bl.makedirs')
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.join')
@mock.patch('pet.bl.Popen')
@mock.patch('os.path.isfile')
def test_recreate_command(mock_isfile, mock_popen, mock_join, mock_pet_folder, mock_makedirs):
    mock_isfile.return_value = True
    recreate()
    mock_popen.assert_not_called()
    mock_isfile.return_value = False
    recreate()
    mock_popen.assert_called_with(["/bin/sh",
                                   "-c",
                                   "echo \"EDITOR==$EDITOR\" > {0}".format(os.path.join(PET_FOLDER, "config")),
                                   ])


@mock.patch('pet.bl.ProjectLock')
@mock.patch('pet.bl.log.warning')
@mock.patch('pet.bl.how_many_active')
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.path.isfile')
def test_lockable_decorator(mock_isfile, mock_pet_folder, mock_amount_active, mock_log_warning, mock_project_lock, project_names):
    name = project_names[0]

    @lockable()
    def func_to_test1(project_name):
        pass
    mock_isfile.return_value = True
    with pytest.raises(ProjectActivated):
        func_to_test1(project_name=name)

    @lockable(check_active=True)
    def func_to_test2(project_name):
        pass
    mock_isfile.return_value = False
    mock_amount_active.return_value = 3
    with pytest.raises(ProjectActivated):
        func_to_test2(project_name=name)

    @lockable(check_only_projects=False)
    def func_to_test3(project_name, arg1, arg2, kwarg=''):
        return project_name, arg1, arg2, kwarg
    assert func_to_test3(project_name=name, arg1=1, arg2=2, kwarg='x') == (name, 1, 2, 'x')
    mock_log_warning.assert_called_with(ExceptionMessages.project_is_active.value.format(name))
    assert mock_project_lock.called

    @lockable()
    def func_to_test4(project_name, arg1, arg2, kwarg=''):
        return project_name, arg1, arg2, kwarg

    assert func_to_test4(project_name=name, arg1=1, arg2=2, kwarg='x') == (name, 1, 2, 'x')

    assert func_to_test4(project_name=name, arg1=1, arg2=2, kwarg='x', lock=True) == (name, 1, 2, 'x')
    mock_log_warning.assert_called_with(ExceptionMessages.project_is_active.value.format(name))

    class ClassToTest1(object):

        def __init__(self, arg1, arg2, kwarg=''):
            self.arg1 = arg1
            self.arg2 = arg2
            self.kwarg = kwarg

        @lockable(check_only_projects=False)
        def action(self, project_name):
            arg3 = self.arg1 + self.arg2
            return project_name, self.arg1, self.arg2, arg3, self.kwarg

    assert ClassToTest1(arg1=1, arg2=2, kwarg='x').action(project_name=name) == (name, 1, 2, 3, 'x')

    class ClassToTest2(object):
        def __init__(self, arg1, arg2, kwarg=''):
            self.arg1 = arg1
            self.arg2 = arg2
            self.kwarg = kwarg

        @lockable()
        def action(self, project_name):
            arg3 = self.arg1 + self.arg2
            return project_name, self.arg1, self.arg2, arg3, self.kwarg

    assert ClassToTest2(arg1=1, arg2=2, kwarg='x').action(project_name=name) == (name, 1, 2, 3, 'x')

    assert ClassToTest2(arg1=1, arg2=2, kwarg='x').action(project_name=name, lock=True) == (name, 1, 2, 3, 'x')
    mock_log_warning.assert_called_with(ExceptionMessages.project_is_active.value.format(name))


# TODO: MOCKING MOCK_OPEN
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
def test_general_shell_mixin_make_rc_file_method(mock_root, mock_pet_folder, project_names):
    project_name = project_names[0]
    project_root = os.path.join(get_projects_root(), project_name)
    nr = 0
    additional_lines = ""
    rc = os.path.join(project_root, "bashrc")
    with mock.patch('%s.open' % builtins_name, create=True) as mock_open:
        Bash().make_rc_file(project_name, nr)
        mock_open.assert_called_with(rc, mode='w')
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_called_with(
            new_project_rc_template.format(
                os.path.join(PET_FOLDER, "bash_profiles"),
                project_name,
                os.path.join(project_root, 'start.sh'),
                nr,
                os.path.join(project_root, 'stop.sh'),
                additional_lines,
                project_name,
            )
        )
    nr = 1
    additional_lines = "cancerous line"
    with mock.patch('%s.open' % builtins_name, create=True) as mock_open:
        Bash().make_rc_file(project_name, nr, additional_lines)
        mock_open.assert_called_with(rc, mode='w')
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_called_with(
            new_project_rc_template.format(
                os.path.join(PET_FOLDER, "bash_profiles"),
                project_name,
                os.path.join(project_root, 'start.sh'),
                "",
                os.path.join(project_root, 'stop.sh'),
                additional_lines,
                project_name,
            )
        )


@mock.patch('os.environ.get', return_value='wrong/shell')
def test_general_shell_mixin_class_errors(mock_get, project_names, task_names):
    project_name = project_names[0]
    task_name = task_names[0]
    project_root = os.path.join(projects_root, project_name)
    with pytest.raises(ShellNotRecognized):
        GeneralShellMixin().start(project_root, project_name)
    with pytest.raises(ShellNotRecognized):
        GeneralShellMixin().create_shell_profiles()
    with pytest.raises(ShellNotRecognized):
        GeneralShellMixin().task_exec(project_name, task_name, interactive=False)
    with pytest.raises(ShellNotRecognized):
        GeneralShellMixin().edit_shell_profiles()


@mock.patch('pet.bl.how_many_active', return_value=3)
@mock.patch('pet.bl.Popen')
@mock.patch('pet.bl.GeneralShellMixin.make_rc_file')
def test_bash_start_method(mock_make_rc_file, mock_popen, mock_how_many_active, project_names):
    project_name = project_names[0]
    project_root = os.path.join(projects_root, project_name)
    Bash().start(project_root, project_name)
    mock_popen.assert_called_with(
        ["/bin/sh",
         "-c",
         "cd {3}\n#pet {0}={1}\n$SHELL --rcfile {2}\nprintf ''".format(
             project_name,
             3 + 1,
             os.path.join(project_root, "bashrc"),
             project_root,
         )
         ]
    )
    assert mock_make_rc_file.called


@mock.patch('os.path.isfile', side_effect=[False, True, True, True])
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
def test_bash_create_shell_profiles_method(mock_pet_folder, mock_isfile):
    with mock.patch('%s.open' % builtins_name, create=True) as mock_open:
        Bash().create_shell_profiles()
        mock_open.assert_called_with(os.path.join(PET_FOLDER, "bash_profiles"), mode='w')
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_has_calls([
            mock.call("source ~/.bashrc\n"),
            mock.call("source ~/.profile\n"),
            mock.call("source ~/.bash_profile\n"),
        ])


@mock.patch('os.path.isfile', side_effect=[False, False, True, True, True])
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('pet.bl.how_many_active', return_value=3)
@mock.patch('pet.bl.GeneralShellMixin.make_rc_file')
@mock.patch('pet.bl.get_file_fullname_and_path', return_value='/some/path/file.ext')
@mock.patch('pet.bl.Popen')
@mock.patch('os.chmod')
def test_bash_task_exec_method(mock_chmod, mock_popen, mock_path, mock_make_rc_file, mock_how_many_active, mock_pet_folder, mock_projects_root, mock_isfile, project_names, task_names):
    project_name = project_names[0]
    task_name = task_names[0]
    project_root = os.path.join(get_projects_root(), project_name)
    tasks_root = os.path.join(project_root, "tasks")
    Bash().task_exec(project_name=project_name, task_name=task_name, interactive=True)
    mock_make_rc_file.assert_called_with(project_name, nr=1, additional_lines=task_exec_template.format(
                '/some/path/file.ext',
                " ".join(()),
                os.path.join(tasks_root, task_name + ".local.entry.sh"),
                os.path.join(tasks_root, task_name + ".local.exit.sh"),
                "",
            ), prompt=project_name + " - " + task_name)
    mock_popen.assert_called_with(["/bin/bash", "-c", "cd {3}\n#pet {0}={1}\n$SHELL --rcfile {2}\nprintf ''".format(
                project_name,
                3 + 1,
                os.path.join(project_root, "bashrc"),
                project_root,
            )])
    Bash().task_exec(project_name=project_name, task_name=task_name, interactive=False)
    mock_make_rc_file.assert_called_with(project_name, nr=1, additional_lines=task_exec_template.format(
                '/some/path/file.ext',
                " ".join(()),
                os.path.join(tasks_root, task_name + ".local.entry.sh"),
                os.path.join(tasks_root, task_name + ".local.exit.sh"),
                "exit",
            ), prompt=project_name + " - " + task_name)
    mock_popen.assert_called_with(["/bin/bash", "-c", "cd {3}\n#pet {0}={1}\n$SHELL --rcfile {2}\nprintf ''".format(
                project_name,
                3 + 1,
                os.path.join(project_root, "bashrc"),
                project_root,
            )])


@mock.patch('pet.bl.edit_file')
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
def test_bash_edit_shell_profiles_method(mock_pet_folder, mock_edit):
    Bash().edit_shell_profiles()
    mock_edit.assert_called_with(os.path.join(PET_FOLDER, "bash_profiles"))


@mock.patch('pet.bl.how_many_active', return_value=3)
@mock.patch('pet.bl.Popen')
@mock.patch('pet.bl.GeneralShellMixin.make_rc_file')
def test_zsh_start_method(mock_make_rc_file, mock_popen, mock_how_many_active, project_names):
    project_name = project_names[0]
    project_root = os.path.join(projects_root, project_name)
    Zsh().start(project_root, project_name)
    mock_popen.assert_called_with(
        ["/bin/sh",
         "-c",
         "cd {2}\n#pet {0}={1}\nZDOTDIR={2} $SHELL\nprintf ''".format(
             project_name,
             3 + 1,
             project_root,
         )
         ]
    )
    assert mock_make_rc_file.called


@mock.patch('os.path.isfile', return_value=False)
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('os.environ.get')
def test_zsh_create_shell_profiles_method(mock_get, mock_pet_folder, mock_isfile):
    mock_get.return_value = "/zdotpath/"
    with mock.patch('%s.open' % builtins_name, create=True) as mock_open:
        Zsh().create_shell_profiles()
        mock_open.assert_called_with(os.path.join(PET_FOLDER, "zsh_profiles"), mode='w')
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_called_with("source $ZDOTDIR/.zshrc\n")
    mock_get.return_value = ""
    with mock.patch('%s.open' % builtins_name, create=True) as mock_open:
        Zsh().create_shell_profiles()
        mock_open.assert_called_with(os.path.join(PET_FOLDER, "zsh_profiles"), mode='w')
        handle = mock_open.return_value.__enter__.return_value
        handle.write.assert_called_with("source $HOME/.zshrc\n")


@mock.patch('os.path.isfile', side_effect=[False, False, True, True, True])
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
@mock.patch('pet.bl.how_many_active', return_value=3)
@mock.patch('pet.bl.GeneralShellMixin.make_rc_file')
@mock.patch('pet.bl.get_file_fullname_and_path', return_value='/some/path/file.ext')
@mock.patch('pet.bl.Popen')
@mock.patch('os.chmod')
def test_zsh_task_exec_method(mock_chmod, mock_popen, mock_path, mock_make_rc_file, mock_how_many_active, mock_pet_folder, mock_projects_root, mock_isfile, project_names, task_names):
    project_name = project_names[0]
    task_name = task_names[0]
    project_root = os.path.join(projects_root, project_name)
    tasks_root = os.path.join(project_root, "tasks")
    Zsh().task_exec(project_name=project_name, task_name=task_name, interactive=True)
    mock_make_rc_file.assert_called_with(project_name, nr=1, additional_lines=task_exec_template.format(
                '/some/path/file.ext',
                " ".join(()),
                os.path.join(tasks_root, task_name + ".local.entry.sh"),
                os.path.join(tasks_root, task_name + ".local.exit.sh"),
                "",
            ), prompt=project_name + " - " + task_name)
    mock_popen.assert_called_with(["/bin/zsh",
                                   "-c",
                                   "cd {2}\n#pet {0}={1}\nZDOTDIR={2} $SHELL\nprintf ''".format(
                                       project_name,
                                       3 + 1,
                                       project_root,
                                   )])
    Zsh().task_exec(project_name=project_name, task_name=task_name, interactive=False)
    mock_make_rc_file.assert_called_with(project_name, nr=1, additional_lines=task_exec_template.format(
                '/some/path/file.ext',
                " ".join(()),
                os.path.join(tasks_root, task_name + ".local.entry.sh"),
                os.path.join(tasks_root, task_name + ".local.exit.sh"),
                "exit",
            ), prompt=project_name + " - " + task_name)
    mock_popen.assert_called_with(["/bin/zsh", "-c", "cd {2}\n#pet {0}={1}\nZDOTDIR={2} $SHELL\nprintf ''".format(
                project_name,
                3 + 1,
                project_root,
            )])


@mock.patch('pet.bl.edit_file')
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
def test_zsh_edit_shell_profiles_method(mock_pet_folder, mock_edit):
    Zsh().edit_shell_profiles()
    mock_edit.assert_called_with(os.path.join(PET_FOLDER, "zsh_profiles"))


@mock.patch('pet.bl.lru_cache')
@mock.patch('os.environ.get')
def test_get_shell_command(mock_get, mock_lru, shells):
    side = shells
    mock_get.side_effect = side
    for i in range(len(shells)):
        assert isinstance(get_shell(), GeneralShellMixin)


@mock.patch('os.path.exists')
@mock.patch('os.remove')
@mock.patch('pet.bl.open')
@mock.patch('os.path.join')
@mock.patch('pet.bl.get_projects_root')
def test_project_lock_class(mock_root, mock_join, mock_open, mock_remove, mock_exists, project_names):
    mock_exists.return_value = True
    project_name = project_names[0]
    with ProjectLock(project_name):
        mock_open.assert_called_with(mock_join(), "w")
    mock_remove.assert_called_with(mock_join())
    mock_exists.return_value = False
    with pytest.raises(NameNotFound):
        ProjectLock("not_existing")


@mock.patch('pet.bl.project_template_exist')
@mock.patch('pet.bl.project_exist')
@mock.patch('pet.bl.get_projects_templates_root', return_value=projects_templates_root)
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.path.exists')
@mock.patch('os.path.isfile', return_value=True)
@mock.patch('pet.bl.get_shell')
@mock.patch('os.getcwd', return_value="")
@mock.patch('os.symlink')
@mock.patch('pet.bl.open')
@mock.patch('os.makedirs')
@mock.patch('pet.bl.get_pet_folder', return_value=PET_FOLDER)
def test_project_creator_class(mock_pet_folder, mock_makedirs, mock_open, mock_symlink, mock_getcwd, mock_shell, mock_isfile, mock_path_exists, mock_root, mock_templates_root, mock_project_exist, mock_template_exist, project_names, additional_project_names):
    project_name = project_names[0]
    project_root = os.path.join(projects_root, project_name)
    templates = [additional_project_names[0], additional_project_names[1]]
    mock_project_exist.return_value = True
    mock_path_exists.return_value = True

    # check_templates

    with pytest.raises(NameAlreadyTaken):
        ProjectCreator(project_name=project_name, in_place=False, templates=templates).create()
    mock_project_exist.return_value = False
    with pytest.raises(NameAlreadyTaken):
        ProjectCreator(project_name='init', in_place=False, templates=templates).create()
    mock_template_exist.return_value = False
    mock_project_exist.side_effect = [False, True, True]
    ProjectCreator(project_name=project_name, in_place=True, templates=templates).create()
    mock_project_exist.side_effect = [False, False]
    with pytest.raises(NameNotFound):
        ProjectCreator(project_name=project_name, in_place=True, templates=templates).create()
    mock_template_exist.return_value = True
    mock_project_exist.side_effect = [False]
    ProjectCreator(project_name=project_name, in_place=True, templates=templates).create()

    # next

    mock_path_exists.return_value = False
    mock_project_exist.side_effect = [False]
    with mock.patch('%s.open' % builtins_name, create=True) as mock_open:
        ProjectCreator(project_name=project_name, in_place=True, templates=templates).create()
        assert mock_shell().create_shell_profiles.called
        assert mock_makedirs.called
        assert mock_symlink.called
        assert mock_shell().make_rc_file.called


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.get_shell')
@mock.patch('os.path.isfile')
def test_start_command(mock_isfile, mock_shell, mock_projects_root, project_names):
    project_name = project_names[0]
    mock_isfile.return_value = True
    with pytest.raises(ProjectActivated):
        start(project_name)
    project_name = project_names[1]
    project_root = os.path.join(projects_root, project_name)
    mock_isfile.return_value = False
    start(project_name=project_name)
    assert mock_shell().create_shell_profiles.called
    mock_shell().start.assert_called_with(project_root, project_name)


def test_create_command():
    pass


@mock.patch('pet.bl.ProjectCreator')
def test_create_command(mock_project_creator, project_names):
    project_name = project_names[0]
    create(project_name, in_place=False, templates=())
    assert mock_project_creator().create.called


@mock.patch('os.getcwd', return_value="/some/path")
@mock.patch('os.path.basename', return_value="project")
@mock.patch('pet.bl.project_exist')
@mock.patch('os.path.isfile')
@mock.patch('os.path.isdir')
@mock.patch('os.symlink')
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.edit_file')
def test_register_command(mock_edit, mock_root, mock_symlink, mock_isdir, mock_isfile, mock_exist, mock_basename, mock_getcwd):
    mock_exist.side_effect = [True]
    with pytest.raises(NameAlreadyTaken):
        register("x")
    mock_exist.side_effect = [False, False]
    mock_isdir.return_value = True
    mock_isfile.return_value = False
    with pytest.raises(PetException):
        register("x")
    mock_isfile.return_value = True
    with pytest.raises(Info):
        register("x")


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.path.exists')
@mock.patch('os.rename')
def test_rename_project_command(mock_rename, mock_exists, mock_root, project_names):
    project_name = project_names[0]
    mock_exists.side_effect = [False]
    with pytest.raises(NameNotFound):
        rename_project("old", project_name)
    mock_exists.side_effect = [True, True]
    with pytest.raises(NameAlreadyTaken):
        rename_project("old", project_name)
    mock_exists.side_effect = [True, False]
    rename_project("old", project_name)
    mock_rename.assert_called_with(os.path.join(projects_root, "old"),
                                   os.path.join(projects_root, project_name))


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.project_exist')
@mock.patch('pet.bl.edit_file')
def test_edit_project_command(mock_edit_file, mock_exist, mock_root, project_names):
    project_name = project_names[0]
    mock_exist.return_value = False
    with pytest.raises(NameNotFound):
        edit_project(project_name)
    mock_exist.return_value = True
    edit_project(project_name)
    mock_edit_file.assert_has_calls([
        mock.call(os.path.join(projects_root, project_name, "start.sh")),
        mock.call(os.path.join(projects_root, project_name, "stop.sh")),
    ])


@mock.patch('os.kill')
def test_stop_command(mock_kill):
    stop()
    assert mock_kill.called

# TODO: 7th


@mock.patch('pet.bl.lockable', return_value=lockable_t)
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.path.exists')
@mock.patch('os.path.islink')
@mock.patch('os.remove')
@mock.patch('pet.bl.shutil.rmtree')
def test_remove_project_command(mock_rmtree, mock_remove, mock_islink, mock_exists, mock_root, mock_lockable, project_names):
    project_name = project_names[0]
    mock_exists.return_value = False
    with pytest.raises(NameNotFound):
        remove_project(project_name=project_name)
    mock_exists.return_value = True
    mock_islink.return_value = True
    remove_project(project_name=project_name)
    mock_islink.return_value = False
    remove_project(project_name=project_name)


@mock.patch('pet.bl.lockable', return_value=lockable_t)
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.path.exists')
@mock.patch('pet.bl.shutil.move')
@mock.patch('pet.bl.get_archive_root', return_value=archive_root)
@mock.patch('pet.bl.print_old')
def test_archive_project_command(mock_old, mock_root_archive, mock_move, mock_exists, mock_root, mock_lockable, project_names):
    project_name = project_names[0]
    mock_exists.return_value = False
    with pytest.raises(NameNotFound):
        archive(project_name=project_name)
    mock_exists.return_value = True
    mock_old.return_value = "cancer\n{0}".format(project_name)
    with pytest.raises(NameAlreadyTaken):
        archive(project_name=project_name)
    mock_old.return_value = ""
    archive(project_name=project_name)


@mock.patch('pet.bl.shutil.copy')
@mock.patch('pet.bl.get_projects_templates_root', return_value=projects_templates_root)
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.project_template_exist')
@mock.patch('os.path.exists')
def test_add_to_templates(mock_exists, mock_template_exists, mock_root, mock_templates_root, mock_copy, project_names):
    project_name = project_names[0]
    project_root = os.path.join(projects_root, project_name)
    mock_exists.return_value = False
    with pytest.raises(NameNotFound):
        add_to_templates(project_name)
    mock_exists.return_value = True
    mock_template_exists.return_value = True
    with pytest.raises(NameAlreadyTaken):
        add_to_templates(project_name)
    mock_template_exists.return_value = False
    add_to_templates(project_name)
    mock_copy.assert_called_with(project_root, os.path.join(projects_templates_root, project_name))


@mock.patch('pet.bl.shutil.move')
@mock.patch('pet.bl.project_exist')
@mock.patch('pet.bl.get_archive_root', return_value=archive_root)
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.path.exists')
def test_restore_command(mock_exists, mock_root, mock_archive_root, mock_project_exist, mock_move, project_names):
    project_name = project_names[0]
    mock_exists.return_value = False
    with pytest.raises(NameNotFound):
        restore(project_name)
    mock_exists.return_value = True
    mock_project_exist.return_value = True
    with pytest.raises(NameAlreadyTaken):
        restore(project_name)
    mock_project_exist.return_value = False
    restore(project_name)
    mock_move.assert_called_with(os.path.join(archive_root, project_name), os.path.join(projects_root, project_name))


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.listdir', return_value=["test_project", "test_project_2", "test_project_3"])
@mock.patch('os.path.exists')
@mock.patch('os.remove')
def test_clean_command(mock_remove, mock_exists, mock_listdir, mock_root):
    clean()
    calls = []
    for project in ["test_project", "test_project_2", "test_project_3"]:
        calls.append(mock.call(os.path.join(projects_root, project, "_lock")))
    for call in calls:
        assert call in mock_remove.mock_calls


@mock.patch('os.path.isdir', return_value=True)
@mock.patch('os.listdir', return_value=['one', 'two', 'three'])
def test_print_projects_for_root(mock_listdir, mock_isdir):
    assert print_projects_for_root("some/root") == "one\ntwo\nthree"


@mock.patch('pet.bl.print_projects_for_root')
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
def test_print_list_command(mock_root, mock_print):
    print_list()
    mock_print.assert_called()


@mock.patch('pet.bl.print_projects_for_root')
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
def test_print_old_command(mock_root, mock_print):
    print_old()
    mock_print.assert_called()


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('os.listdir', return_value=['one.txt', 'two.py', 'three.sh'])
def test_print_tasks_command(mock_listdir, mock_root, project_names):
    project_name = project_names[0]
    assert print_tasks(project_name) == "one\ntwo\nthree"


def test_print_tree_command():
    pass


@mock.patch('pet.bl.print_projects_for_root')
@mock.patch('pet.bl.get_projects_templates_root', return_value=projects_templates_root)
def test_print_templates_command(mock_root, mock_print):
    print_templates()
    mock_print.assert_called()


@mock.patch('pet.bl.project_exist')
@mock.patch('pet.bl.task_exist')
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.Popen')
@mock.patch('pet.bl.edit_file')
@mock.patch('pet.bl.open')
@mock.patch('os.chmod')
def test_create_task_command(mock_chmod, mock_open, mock_edit_file, mock_popen, mock_root, mock_task_exist, mock_project_exist, project_names, task_names):
    project_name = project_names[0]
    project_root = os.path.join(projects_root, project_name)
    mock_project_exist.return_value = False
    with pytest.raises(NameNotFound):
        create_task(project_name, task_names[0], no_alias=True, how='save')
    mock_project_exist.return_value = True
    mock_task_exist.return_value = True
    with pytest.raises(NameAlreadyTaken):
        create_task(project_name, task_names[0], no_alias=True, how='save')
    mock_project_exist.return_value = True
    mock_task_exist.return_value = False
    task_name = 'task.py'
    with pytest.raises(Info):
        create_task(project_name, task_name, no_alias=True, how='save')
    task_file_path = os.path.join(project_root, "tasks", task_name)
    task_name = os.path.splitext(task_name)[0]
    mock_popen.assert_called_with(["/bin/sh", "-c", "echo 'add shebang to make sure file will be executable' > {0}".format(task_file_path)])
    mock_edit_file.assert_called_with(task_file_path)
    task_name = 'task'
    with pytest.raises(Info):
        create_task(project_name, task_name, no_alias=True, how='save')
    task_file_path = os.path.join(project_root, "tasks", task_name + ".sh")
    task_name = os.path.splitext(task_name)[0]
    mock_popen.assert_called_with(["/bin/sh", "-c", "echo '#!/bin/sh' > {0}".format(task_file_path)])
    mock_edit_file.assert_called_with(task_file_path)


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.get_file_fullname_and_path')
@mock.patch('pet.bl.edit_file')
@mock.patch('pet.bl.task_exist')
def test_edit_task_command(mock_exist, mock_edit, mock_fullpath, mock_root, project_names, task_names):
    project_name = project_names[0]
    task_name = task_names[0]
    mock_exist.return_value = False
    with pytest.raises(NameNotFound):
        edit_task(project_name, task_name)
    mock_exist.return_value = True
    edit_task(project_name, task_name)
    mock_edit.assert_called_with(mock_fullpath())


@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.get_file_fullname_and_path', return_value='sth.ext')
@mock.patch('pet.bl.task_exist')
@mock.patch('os.rename')
def test_rename_task_command(mock_rename, mock_task_exist, mock_fullpath, mock_root, project_names, task_names):
    project_name = project_names[0]
    tasks_root = os.path.join(projects_root, project_name, "tasks")
    mock_task_exist.return_value = False
    with pytest.raises(NameNotFound):
        rename_task(project_name, task_names[0], task_names[1])
    mock_task_exist.return_value = True
    with pytest.raises(NameAlreadyTaken):
        rename_task(project_name, task_names[0], task_names[1])
    mock_task_exist.side_effect = [True, False]
    rename_task(project_name, task_names[0], task_names[1])
    mock_rename.assert_called_with(mock_fullpath(), os.path.join(tasks_root, task_names[1] + ".ext"))


@mock.patch('pet.bl.get_shell')
@mock.patch('os.path.isfile')
@mock.patch('pet.bl.task_exist')
def test_run_task_command(mock_exist, mock_isfile, mock_shell, project_names, task_names):
    project_name = project_names[0]
    mock_exist.return_value = False
    with pytest.raises(NameNotFound):
        run_task(project_name, task_names[0], interactive=False, args=())
    mock_exist.return_value = True
    mock_isfile.return_value = False
    run_task(project_name, task_names[0], interactive=False, args=())
    assert mock_shell().create_shell_profiles.called
    mock_shell().task_exec.assert_called_with(project_name, True, task_names[0], False, ())


@mock.patch('pet.bl.get_file_fullname')
@mock.patch('pet.bl.get_file_fullname_and_path')
@mock.patch('pet.bl.get_projects_root', return_value=projects_root)
@mock.patch('pet.bl.task_exist')
@mock.patch('pet.bl.Popen')
@mock.patch('pet.bl.PIPE')
@mock.patch('os.remove')
def test_remove_task_command(mock_remove, mock_pipe, mock_popen, mock_exist, mock_root, mock_fullpath, mock_fullname, project_names, task_names):
    project_name = project_names[0]
    project_root = os.path.join(projects_root, project_name)
    mock_fullname.return_value = task_names[0]
    mock_exist.return_value = False
    with pytest.raises(NameNotFound):
        remove_task(project_name, task_names[0])
    mock_exist.return_value = True
    mock_popen.stdout.read().return_value = b'6\n'
    remove_task(project_name, task_names[0])
    mock_popen.assert_called_with([
        "/bin/sh",
        "-c",
        "sed -i -e \"/alias {0}/d\" {1}".format(
            task_names[0],
            os.path.join(project_root, "start.sh"),
        )
    ])
    mock_remove.assert_called_with(mock_fullpath())


@mock.patch('pet.bl.get_pet_install_folder', return_value=PET_INSTALL_FOLDER)
@mock.patch('pet.bl.edit_file')
def test_edit_config_command(mock_edit, mock_folder):
    edit_config()
    assert mock_edit.called


@mock.patch('pet.bl.get_pet_install_folder', return_value=PET_INSTALL_FOLDER)
@mock.patch('pet.bl.get_shell')
def test_edit_shell_profiles_command(mock_shell, mock_folder):
    edit_shell_profiles()
    assert mock_shell().edit_shell_profiles.called


def test_deploy_command():
    pass
