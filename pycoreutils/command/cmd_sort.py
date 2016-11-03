from __future__ import print_function, unicode_literals
import pycoreutils
import pycoreutils.lib


def parseargs(p):
    '''
    Add arguments and `func` to `p`.

    :param p: ArgumentParser
    :return:  ArgumentParser
    '''
    # TODO: GNU's sort doesn't count '/'.
    # Sorting /etc/fstab has different outcomes.
    p.set_defaults(func=func)
    p.description = "sort lines of text files"
    p.add_argument('FILE', nargs='*')
    p.add_argument("-r", "--reverse", action="store_true", dest="reverse",
            help="reverse the result of comparisons")
    return p


def func(args):
    l = []
    for line, filename in pycoreutils.lib.parsefilelist(args.FILE):
        l.append(line)
    l.sort(reverse=args.reverse or False)
    print(''.join(l), end='')
