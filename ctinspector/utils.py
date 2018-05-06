from __future__ import print_function
import six
from ctinspector.colorhelper import print_info, print_header, info, info_header, term_columns

def print_list(label, items):
    if not items:
        return
    print_header("_" * term_columns())
    print_header(label)
    if isinstance(items, (list, tuple)):
        for item in items:
            print_info("\t"+item)
    if isinstance(items, dict):
        for key, value in items.items():
            if value:
                if isinstance(value, six.string_types):
                    print('{0:>15}: {1}'.format(key, info(value)))
                if isinstance(value, list):
                    print('{0:>15}:'.format(key))
                    for value_item in value:
                        print(' '*15, info(value_item))
                if isinstance(value, dict):
                    print('{0:>15}:'.format(key))
                    for dict_key, dict_value in value.items():
                        print(' '*16+'{0:>15}: {1}'.format(info_header(dict_key), info(dict_value)))
    print_header("_" * term_columns())
