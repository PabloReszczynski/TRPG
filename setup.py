import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

requirements = []

dev_requirements = [
    'behave',
    'sure'
]

setup(
    name = 'TRPG',
    version = '0.0.1',
    author = 'Pablo Reszczynski',
    author_email = 'pablore@me.com',
    description = 'A tactical rpg made in my free time',
    license = 'MIT',
    url = 'github.com/pabloreszczynski/TRPG',
    packages = find_packages(),
    install_requirements = requirements,
    extras_require = {
        'dev': dev_requirements
    },
    long_description=read('README.md')
)
