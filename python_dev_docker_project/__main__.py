from __future__ import print_function

import sys

from python_dev_docker_project.hello import hello


def main(argv=sys.argv[1:]):
    print(hello(' '.join(argv)))


if __name__ == '__main__':
    main()
