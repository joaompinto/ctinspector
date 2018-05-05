#! /usr/bin/env python
"""ctrust

Usage:
    ctrust ( image <image_name> | container <container_id> )

Options:
    -h --help     Show this screen.
"""
import sys
from docopt import docopt
from os.path import join, dirname, realpath
from colorama import init
from ctrust import report


# Make sure we use the source directory for imports when running during development
script_dir = join(dirname(realpath(__file__)), '..')
sys.path.insert(0, script_dir)
from ctrust import version


def main():
    init()
    #  client = docker.from_env()
    arguments = docopt(__doc__, version='ctrust %s' % version())
    if arguments['image']:
        image_name = arguments['<image_name>']
        report.image(image_name)
    if arguments['container']:
        container_id = arguments['<container_id>']
        report.container(container_id)


if __name__ == "__main__":
    main()
