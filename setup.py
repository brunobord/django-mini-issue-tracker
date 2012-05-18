from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='issuetracker',
    version='1.0',
    author='Bruno Bord',
    author_email='bruno@jehaisleprintemps.net',
    packages=find_packages(),
    description='Using the automagic django admin site to track issues.',
    url='https://github.com/brunobord/django-mini-issue-tracker',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    license='Unknown',
)
