#!/usr/bin/env python
from distutils.command.install_scripts import install_scripts
from distutils.core import setup

from setuptools import find_packages

requirements = [
    line.split('==')[0]
    for line in open('requirements.txt', 'r').readlines()
]


class InstallScripts(install_scripts):
    def run(self):
        print("This line will never be printed")

    def get_outputs(self):
        return []


setup(
    name='pet',
    version='0.0.1',
    description='Project Environment Tool',
    author='LimeBrains',
    author_email='mail@limebrains.com',
    url='https://github.com/limebrains/pet',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points="""\
      [console_scripts]
      pet = pet.cli:main
    """,
    cmdclass={'install_scripts': InstallScripts},
    scripts=[],
)
