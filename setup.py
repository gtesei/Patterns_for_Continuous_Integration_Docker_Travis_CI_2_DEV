import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):  # Stolen from txacme
    with open(os.path.join(HERE, *parts)) as f:
        return f.read()


setup(
    name='python-dev-docker-project',
    version='0.5.3.dev0',
    license='BSD-3-Clause',
    url='https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV',
    description='',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    author='Gino Tesei',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello = python_dev_docker_project.__main__:main',
        ]
    }
)
