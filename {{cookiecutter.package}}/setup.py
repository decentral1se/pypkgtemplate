from setuptools import find_packages, setup

with open('README.rst', 'r') as handle:
    long_description = handle.read()

# TODO: librefund hooks

setup(
    name='{{cookiecutter.package}}',
    version='0.0.1',
    url='{{cookiecutter.git_hosting_url}}',
    license='GPLv3',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    description='{{cookiecutter.package_description}}',
    long_description=long_description,
    packages=find_packages(exclude=['test']),
    install_requires=[],
)
