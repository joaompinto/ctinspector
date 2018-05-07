from __future__ import print_function
import six
from ctinspector.colorhelper import print_info, print_header, info, info_header, term_columns

def print_list_value(key, value):
    if isinstance(value, (six.string_types, int)):
        print('{0:>15}: {1}'.format(key, info(value)))
    if isinstance(value, list):
        print('{0:>15}:'.format(key))
        for value_item in value:
            if value_item in [None, ""]:
                continue
            print(' '*15, info(value_item))
    if isinstance(value, dict):
        print('{0:>15}:'.format(key))
        for dict_key, dict_value in value.items():
            if dict_value in [None, "", [], {}]:
                continue
            print(' '*16+'{0:>15}: {1}'.format(info_header(dict_key), info(dict_value)))

def print_list(label, items, with_split=False):
    if not items:
        return
    if with_split:
        print_header("_" * term_columns())
    print_header(label)
    if isinstance(items, (list, tuple)):
        for item in items:
            print_info("\t"+item)
    if isinstance(items, dict):
        for key, value in items.items():
            if value:
                print_list_value(key, value)

    if with_split:
        print_header("_" * term_columns())

def human_size(bytes, units=[' bytes', ' KB', ' MB', ' GB', ' TB', ' PB', ' EB']):  # pylint: disable=W0102
    """ Returns a human readable string reprentation of bytes"""
    return str(bytes) + units[0] if bytes < 1024 else human_size(bytes>>10, units[1:])
