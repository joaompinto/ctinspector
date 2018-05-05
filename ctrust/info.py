from __future__ import print_function
from colorhelper import info


def print_image_info(json_data):
    """ print most relevant info extracted from the json data """
    env_entries = json_data['Config'].get("Env")
    mb_size = '{0:.2f}'.format(float(json_data['Size']/(1000.0*1000)))
    print(" Repository: %s" % info(json_data['RepoTags'][0]))
    print("       Size: %s" % info(str(mb_size))+" MB")
    if env_entries:
        print("Environment:\n\t%s" % info("\n\t".join(env_entries)))
