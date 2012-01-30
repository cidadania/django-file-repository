import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-file-repository",
    version = "0.2b",
    author = "Oscar Carballal Prego",
    author_email = "oscar.carballal@cidadania.coop",
    description = ("Simple file repository with public/private files, tags and categories."),
    license = "GPLv3",
    keywords = "repository tagging categorization file",
    url = "http://github.com/cidadania/django-file-repository",
    packages=['repository'],
    long_description=read('README'),
    classifiers=[
        "Development Status :: 4 - Beta/Testing",
        "Topic :: Web Utilities",
        "Framework :: Django 1.3.1",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Natural Language :: Spanish",
        "Dependencies :: django-registration, django-taggit",
        "Intended Audience :: Everyone",
   ],
)
