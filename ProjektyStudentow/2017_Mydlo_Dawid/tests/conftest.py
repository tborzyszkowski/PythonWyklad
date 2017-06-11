import os

import pytest

PET_INSTALL_FOLDER = os.path.join(os.path.dirname(os.path.dirname(__file__)), "pet")
PET_FOLDER = os.environ.get('PET_FOLDER', os.path.join(os.path.expanduser("~"), ".pet/"))
projects_root = os.path.join(PET_FOLDER, "projects")
archive_root = os.path.join(PET_FOLDER, "archive")
templates_root = os.path.join(PET_FOLDER, "templates")


@pytest.fixture
def project_names():
    return ["1test_project", "2test_project", "3test_project", "4", "5_"]


@pytest.fixture
def task_names():
    return ["1hello", "2bye", "task_3", "task_4", "task_5"]


@pytest.fixture
def additional_project_names():
    return ["1project_with_templates", "2project_with_templates"]


@pytest.fixture
def shells():
    return ['bash', 'zsh', '/bin/bash', '/bin/zsh']


@pytest.fixture
def file_names():
    return ["start.sh", "stop.sh"]


@pytest.fixture
def all_project_files():
    return ["start.sh", "stop.sh", "tasks.py", "tasks.sh"]


@pytest.fixture
def files():
    output = []
    for project in project_names():
        for file_name in file_names():
            output.append("{0}/{1}/{2}".format(projects_root, project, file_name))
    return output
