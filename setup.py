from setuptools import setup, find_packages

setup(
    name='coding-agent',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'flask',
        'requests',
        'pytest'
    ],
)