# Patterns for Continuous Integration with Docker using Travis CI 2 - Prod. Repo

[![Build Status](https://api.travis-ci.org/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD.svg?branch=master)](https://travis-ci.org/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD)

![Conceptual Schema](https://raw.githubusercontent.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD/master/img/end-to-end-flow.png)

__The “Docker repo” pattern__: _create two separate Git repositories: one for Docker release and another for software development. This keeps the Docker-specific code isolated from the actual software. Developers can continue working on the source software as usual, while the production Docker image is developed separately_

This repository is an example of the __Git repository for Docker release__. 

Specifically, we create a separate Git repository specifically for the release Dockerfile. This keeps the Docker-specific code, which could be considered a deployment detail, isolated from the actual software. Developers can continue working on the source software as usual, while the production Docker image is developed separately.

When a new development release (e.g. _0.3.9.dev0_) is ready and tested for production (see [Patterns for Continuous Integration with Docker using Travis CI 2 - Dev. Repo](https://github.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV) for more details), someone updates consequently the requirements.txt file and commits on master. In this way:
- Travis CI builds, tests and packages the software, 
- Travis CI does two new docker development images, e.g. _0.3.9.dev0_ (the image of the development release tagged for production, for archiving purpouse) and _latest_ (the production image of the project), on the Docker Registry, e.g. [Docker Hub](https://hub.docker.com).

## requirements.txt  
 
```txt
python-dev-docker-project==0.3.9.dev0
```


## Dockerfile 
 
```docker
FROM python:3.6-slim

COPY requirements.txt /requirements.txt
RUN pip install --no-cache -r requirements.txt

ENTRYPOINT ["hello"]
CMD ["World"]
```

## .travis.yml  

```yml
sudo: required
services:
  - docker
env:
  global:
    - IMAGE_NAME=gtesei/hello_docker_2
    - REGISTRY_USER=gtesei
    # REGISTRY_PASS=...
    - secure: H8o2BrmikY0e9Gzj1t/Ca1H+hblEv9GC6Qd9MQoN/zxXx0MtiZw3eyCuBO4rpYvX80oeS/e9QM1b4v8OUCsRqGd1nwz4QhRQIRyzh03+n+Sp84qnTqAZvDNbPl0WYDSJyRYFij7SpVP37encJX8ioPaE+YarNn1AGUAVthFOvWhEEeuDGV0lDOXw0j+LsXr1hf821dqvlFLBXPE0dVB6LZD2QEde4BaCQaM+FgBRrcz/bkLMBByviUxdCevJsHSOnhc4rZCbBZ5k5oByJsXVMX/S+SFwP5N4ljkF9rjtIA8fMOlGjk8Z8kXSk3BeLctXGSrZBZBsXG2e89AfBeXFrK91tYdLJROXWdd6MN+U9r+FSIblHqB51zE2zFUpXK9pijUeJLNC2eacdNMRTvxA+tudEIuGkIKkgA4aGw8knoroWXI8ByLtVJA2mXQvlMqiN+pVQt36rwx1Tz0mlw2QOsI713f/JhSoJQNX7flRJrcs2FroCCmDrnpXiE+FN+svjLKz7b07lzw8H78PGfj11YPV8LGDHMRqf0/fu55157QaDgoDKekBLuwXYGT+q5pOu91r+9ywIUo5V8WXel7VM1iUqu3Kjq8DLpwiTErENwEEoq8x5uATXAHsnoXEpBFSj6RsU1BdambMkoz7bbOgviVwTDTGB4jgX7iYdlEYdzA=
before_script:
  - version="$(sed -nE 's/^blog-travis-docker==(\S+).*/\1/p' requirements.txt)"
  - docker pull "$IMAGE_NAME" || true
script:
  - docker build --pull --cache-from "$IMAGE_NAME" --tag "$IMAGE_NAME" .
  - docker run "$IMAGE_NAME"

after_script:
  - docker images

before_deploy:
  - docker login -u "$REGISTRY_USER" -p "$REGISTRY_PASS"
  - docker tag "$IMAGE_NAME" "${IMAGE_NAME}:latest"
  - docker tag "$IMAGE_NAME" "${IMAGE_NAME}:${version}"
deploy:
  provider: script
  script: docker push "${IMAGE_NAME}:latest" && docker push "${IMAGE_NAME}:${version}"
  on:
    branch: master
```

### How to encrypt password of Docker Hub on .travis.yml 

![Howto Encrypt Password](https://raw.githubusercontent.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD/master/img/encrypt.PNG)

## Travis CI 

![Travis CI](https://raw.githubusercontent.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD/master/img/travis.PNG)

## Docker Registry [Docker Hub]

![Docker Hub](https://raw.githubusercontent.com/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_PROD/master/img/Docker_Hub.PNG)

## Useful links   

[Ruby Installer for Windows](https://rubyinstaller.org/downloads/)

__To install Travis__ 
```ruby 
gem install travis
```
## Credits 

[Coding Tips: Patterns for Continuous Integration with Docker on Travis CI - Part 2 of 3: The “Docker repo” pattern](https://medium.com/mobileforgood/patterns-for-continuous-integration-with-docker-on-travis-ci-71857fff14c5)

[Defining encrypted variables in .travis.yml](https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml)

[Google Cloud | Continuous Delivery with Travis CI](https://cloud.google.com/solutions/continuous-delivery-with-travis-ci)

[Continuous Integration. CircleCI vs Travis CI vs Jenkins](https://hackernoon.com/continuous-integration-circleci-vs-travis-ci-vs-jenkins-41a1c2bd95f5)

[Continuous Integration with Jenkins and Docker](https://code-maze.com/ci-jenkins-docker/) 

