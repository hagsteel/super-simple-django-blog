import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="simple blog",
    version="0.1.0",
    author="Jonas Hagstedt",
    author_email="hagstedt@gmail.com",
    description=("A VERY basic blog"),
    license="BSD",
    keywords="django blog",
    url = "https://github.com/jonashagstedt/super-simple-django-blog",
    packages=['simple_blog', ],
    long_description=read('README.md'),
    install_requires=[
        "Django >= 1.4",
        "django-taggit",
        "markdown"
    ],
    classifiers=[
        "Development Status :: Beta",
        "Topic :: Blog",
        "License :: OSI Approved :: BSD License",
    ],
)
