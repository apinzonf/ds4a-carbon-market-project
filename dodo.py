import glob
import pytest
from doitpy.coverage import Config, Coverage, PythonPackage

DOIT_CONFIG = {
    'minversion': '0.24.0',
    'default_tasks': ['unit_tests', 'coverage', 'package_zip'],
    'verbosity': 2,
}

TARGET_ZIP_FILE = "build/ds4a-carbon-project.zip"
CODE_FILES = glob.glob("app/*.py")
TEST_FILES = glob.glob("tests/test_*.py")
TESTING_FILES = glob.glob("tests/*.py")
DATA_FILES = glob.glob("data/**/*.*", recursive=True)
ASSETS_FILES = glob.glob("assets/**/*.*", recursive=True)
NOTEBOOKS_FILES = glob.glob("notebooks/**/*.*", recursive=True)
PY_FILES = CODE_FILES + TESTING_FILES
VERSION_FILE = glob.glob("version")


def run_test(test):
    return not bool(pytest.main([test]))


def task_unit_tests():
    """run unit-tests"""
    for test in TEST_FILES:
        yield {'name': test,
               'actions': [(run_test, (test,))],
               'file_dep': PY_FILES}


def task_package_zip():
    """package python files in a zip"""
    return {'actions': ['rm -Rf build',
                        'mkdir -p build',
                        'zip %(targets)s %(dependencies)s'],
            'file_dep': CODE_FILES + DATA_FILES + ASSETS_FILES + NOTEBOOKS_FILES + VERSION_FILE,
            'targets': [TARGET_ZIP_FILE],
            'task_dep': ['unit_tests'],
            'clean': True,
            }


def task_coverage():
    """show coverage for all modules including tests"""
    cov = Coverage([PythonPackage('app', 'tests')],
                   config={'branch': True, 'parallel': True,
                           'omit': []},
                   )
    yield cov.all()
    yield cov.src()
    yield cov.by_module()


def task_create_docker_image():
    return {
        'actions': ['docker build --tag ds4a-carbon-market-project .'],
        'task_dep': ['unit_tests']
    }


def task_push_docker_image():
    return {
        'task_dep': ['create_docker_image'],
        'params': [
            {
                'name': 'registry',
                'short': 'r',
                'long': 'registry',
                'type': str,
                'default': None,
                'help': 'docker registry like some-private-repo.azurecr.io'
            }
        ],
        'actions': [
            'az login',
            'docker login %(registry)s --username 00000000-0000-0000-0000-000000000000 --password '
            '$(az acr login --name %(registry)s --expose-token --output tsv --query accessToken)',
            'docker tag ds4a-carbon-market-project %(registry)s/ds4a-carbon-market-project',
            'docker push %(registry)s/ds4a-carbon-market-project'
        ]
    }
