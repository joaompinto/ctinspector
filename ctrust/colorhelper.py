import sys
import inspect
from termcolor import cprint, colored


def print_error(x):
    return cprint(x, 'red', attrs=['bold'], file=sys.stderr)


def print_info(x):
    return cprint(x, 'cyan')


def print_success(x):
    return cprint(x, 'green', attrs=['bold'])


def print_warn(x):
    return cprint(x, 'yellow', attrs=['bold'], file=sys.stderr)


def info(x):
    return colored(x, 'cyan')


def warning(x):
    return colored(x, 'yellow')


def success(x):
    return colored(x, 'green',  attrs=['bold'])


#  Based on http://stackoverflow.com/a/17412094
def print_template(template, **kwargs):
    "Usage: s(string, **locals())"
    if not kwargs:
        frame = inspect.currentframe()
        try:
            kwargs = frame.f_back.f_locals
        finally:
            del frame
        if not kwargs:
            kwargs = globals()

    print(template.format(**kwargs))
