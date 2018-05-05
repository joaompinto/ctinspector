from __future__ import print_function
import errno
from colorhelper import print_info
from os.path import join, basename
from glob import glob

def show_info(driver):
    print_info("\nDriver", driver['Name'])
    driver_data = driver['Data']
    for key in sorted(driver_data.keys()):
        path_list = driver_data[key]
        for path in path_list.split(':'):
            try:
                content = (glob(join(path, "*")))
            except OSError as err:
                if err.errno == errno.ENOENT:
                    continue
                else:
                    raise
            else:
                if content:
                    print_info(key, path, ' '.join([basename(x) for x in content]))
