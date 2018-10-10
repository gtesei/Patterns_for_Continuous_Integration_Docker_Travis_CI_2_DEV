import os

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):  # Stolen from txacme
    with open(os.path.join(HERE, *parts)) as f:
        return f.read()


setup(
    name='python-dev-docker-project',
    version='0.1.4.dev0',
    license='BSD-3-Clause',
    url='https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV',
    description='',
    long_description=read('README.md'),
    author='Gino Tesei',
    author_email='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'hello = python-dev-docker-project.__main__:main',
        ]
    }
)
