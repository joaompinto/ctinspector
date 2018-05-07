#! /usr/bin/env python
"""

Usage:
    ctinspector ( image <image_name> | container <container_id> )

Options:
    -h --help     Show this screen.
"""
import sys
from docopt import docopt
from os.path import join, dirname, realpath
from colorama import init
from ctinspector import report

# Make sure we use the source directory for imports when running during development
script_dir = join(dirname(realpath(__file__)), '..')
sys.path.insert(0, script_dir)
from ctinspector import version


def main():
    init()
    arguments = docopt(__doc__, version='ctinspector %s' % version())
    if arguments['image']:
        image_name = arguments['<image_name>']
        report.image_info(image_name)
    if arguments['container']:
        container_id = arguments['<container_id>']
        report.container_info(container_id)


if __name__ == "__main__":
    main()
