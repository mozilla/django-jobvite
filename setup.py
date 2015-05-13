from setuptools import setup, find_packages

import django_jobvite


setup(
    name='django-jobvite',
    version=django_jobvite.__version__,
    description='Simpler, JSON based interface to Jobvite',
    long_description=open('README.rst').read(),
    author='Paul Osman',
    author_email='paul@mozillafoundation.org',
    url='http://github.com/mozilla/django-jobvite',
    license='BSD',
    packages=find_packages(),
)
