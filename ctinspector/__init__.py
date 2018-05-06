import os.path


def version():
    """ Return quickweb engine version """

    app_dir = os.path.dirname((os.path.realpath(__file__)))
    version_filename = os.path.join(app_dir, 'version')
    with open(version_filename) as version_file:
        on_file_version = version_file.readline().strip('\r\n')

    return on_file_version
