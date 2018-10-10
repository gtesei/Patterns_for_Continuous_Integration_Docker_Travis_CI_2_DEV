# Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV

[![Build Status](https://api.travis-ci.org/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV.svg?branch=master)](https://travis-ci.org/gtesei/Patterns_for_Continuous_Integration_Docker_Travis_CI_2_DEV)

![Conceptual Schema](./img/end-to-end-flow.png)

__The “Docker repo” pattern__: create two separate Git repositories: one for Docker release and another for software development. This keeps the Docker-specific code isolated from the actual software. Developers can continue working on the source software as usual, while the production Docker image is developed separately.

This repository is an example of the Git repository for software development. 


![Conceptual Schema](./img/end-to-end-flow_2.png)


## Dockerfile 
 
```docker
FROM debian
RUN apt-get update \
    && apt-get install -y --no-install-recommends cowsay \
    && rm -rf /var/lib/apt/lists/*
ENV PATH "$PATH:/usr/games"

ENTRYPOINT ["cowsay"]
CMD ["Hello, World!"]
```

## .travis.yml  

```yml
sudo: required
services:
- docker
env:
  global:
  - REGISTRY_USER=gtesei
  # REGISTRY_PASS=...
    - secret: "<something long>"
before_script:
- docker pull myorg/myimage || true
script:
- docker build --pull --cache-from gtesei/hello_travis --tag gtesei/hello_travis .
- docker run gtesei/hello_travis
after_script:
- docker images
before_deploy:
- docker login -u "$REGISTRY_USER" -p "$REGISTRY_PASS"
deploy:
  provider: script
  script: docker push gtesei/hello_travis
  on:
    branch: master
```


## How to encrypt password of Docker Hub on .travis.yml 

![Howto Encrypt Password](./img/pwd_enc.PNG)

```yml
sudo: required
services:
- docker
env:
  global:
  - REGISTRY_USER=gtesei
  - secret: "<something long>"
  - secure: W8cjk1MzKPXbs+u1PVlP1WPyKOKon0PEeVSf790tV6VtOlExRAK3NPEyFzZ3jjkTsenB/sspBawIJlqjPBQAqeeGz2I7vwWRj1UxawbmHaxaodoclMx3APbg8iW/+qH4bm0M2uyb9F6JWY8azD/j7GKIW8otyIb8s+9qu+wFR9HMuxFuvy8MPABgTk3r6/qflSwWd0QZkia3UqAauFAHCtxTZSwBWz0kL4XBgBEcArVU+1tu6rhOPWsm+CEcxf3WwjCYHdemp5MffC1hWvzgffVWuuFb7Y7ICCCVjaNQ8jgbtJ4HzoFW3vpocRJk7nJiWzTNwXbzqLfreApPEI5ADQqpBczJw23oDG42MiFTurdIXKghzgHo79tDG6ezGRWCkiutcWPu7mgYbWX6og966IboMAOh7aO4zBJY77xkDNYT1YWcrKF3P6Chk7roaGEUJGtZsz/osKzT+XSVdmgOKeQt2fawFlEd7DWAnoDrJwcOWq4NGobR46llQ8YJHHjObS5wzr/ktLvoURDNzTi3RjE4N3nQZvOu57GDcrQ7bkz4if+KNShnkvKg+4DAryB6sSvFaIAtkZmDN1Jf3EgO9eVAKmgGm3AVLzzKsI5NWVIbYqs4Ixp6tFeQ6WF5ad9oeyTVWlov7cDvQclgq0ineO7vgpS5VfqgJQZ6cb92kBg=
before_script:
- docker pull myorg/myimage || true
script:
- docker build --pull --cache-from gtesei/hello_travis --tag gtesei/hello_travis .
- docker run gtesei/hello_travis
after_script:
- docker images
before_deploy:
- docker login -u "$REGISTRY_USER" -p "$REGISTRY_PASS"
deploy:
  provider: script
  script: docker push gtesei/hello_travis
  on:
    branch: master
```

## For each commit on master branch Travis CI builds a new Docker image ...   

![Travis CI](./img/trav_1.PNG)

![Travis CI](./img/trav_2.PNG)

## ... and pushes it on Docker Hub (or different Docker Registry)

![Docker Hub](./img/dock_1.PNG)

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

