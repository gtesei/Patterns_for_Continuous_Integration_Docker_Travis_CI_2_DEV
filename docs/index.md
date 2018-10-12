# Patterns for Continuous Integration

[![Build Status](https://api.travis-ci.org/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV.svg?branch=master)](https://travis-ci.org/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV)
[![PyPI version](https://badge.fury.io/py/python-dev-docker-project.svg)](https://badge.fury.io/py/python-dev-docker-project)
[![Coverage Status](https://coveralls.io/repos/github/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV/badge.svg?branch=master)](https://coveralls.io/github/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV?branch=master)
[![Documentation Status](https://readthedocs.org/projects/patterns-for-continuous-integration-docker-travis-ci-2-dev/badge/?version=latest)](https://patterns-for-continuous-integration-docker-travis-ci-2-dev.readthedocs.io/en/latest/?badge=latest)

## Travis CI 

Focus on Travis CI.  

### [Patterns for Continuous Integration with Docker using Travis CI - Part. 1](https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_1)

__Warming up__: for each commit on the master branch we want to build a Docker image according to a given Dockerfile and push it on Docker Hub (or different Docker Registry) using Travis CI.

![Warming up](https://raw.githubusercontent.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_1/master/img/part_1.png)

### Patterns for Continuous Integration with Docker using Travis CI - Part. 2 

__The “Docker repo” pattern__: _create two separate Git repositories: one for Docker release and another for software development. This keeps the Docker-specific code isolated from the actual software. Developers can continue working on the source software as usual, while the production Docker image is developed separately_

![The “Docker repo” pattern](https://raw.githubusercontent.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV/master/img/end-to-end-flow.png)

This keeps the Docker-specific code, which could be considered a deployment detail, isolated from the actual software. Developers can continue working on the source software as usual, while the production Docker image is developed separately.

#### [Git repository for software development](https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV) 

Team uses different branches for development and, a certain point, pull-requests for merge the master branch are done. For each one of them, committing the master branch:
- modifying the version number in _setup.py_, a new release will be created on the package repository (e.g. [PyPI](https://pypi.org/)), 
- Travis CI builds, tests and packages the software by using __py.test__ and __measuring code coverage of Python code__.
- if such tests are successful: 
    - code coverage stats are published on [coveralls.io](https://coveralls.io/) through [coveralls](https://pypi.org/project/coveralls/),
    - Travis CI does a release of the software by uploading the package to the package repository (e.g. [PyPI](https://pypi.org/)),
    - Travis CI does two new docker development images, e.g. _e59cbe8-develop_ (image for last commit on master branch) and _develop_ (the official develop image of the project), on the Docker Registry, e.g. [Docker Hub](https://hub.docker.com).

#### [Git repository for Docker release](https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD) 

When a new development release (e.g. _0.3.9.dev0_) is ready and tested for production (see [Patterns for Continuous Integration with Docker using Travis CI 2 - Dev. Repo](https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV) for more details), someone updates consequently the requirements.txt file and commits on master. In this way:
- Travis CI builds, tests and packages the software, 
- Travis CI does two new docker development images, e.g. _0.3.9.dev0_ (the image of the development release tagged for production, for archiving purpouse) and _latest_ (the production image of the project), on the Docker Registry, e.g. [Docker Hub](https://hub.docker.com).


