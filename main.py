import argparse
import os
from du import DiskUsage
from view import list_view, tree_view


def main():
    arg_parser = argparse.ArgumentParser('DiskUsage')
    arg_parser.add_argument('path', type=str,
                            help='path to an existing directory')
    arg_parser.add_argument('-a', '--all', action='store_true',
                            help='write counts for all files, not just directories')
    arg_parser.add_argument('-s', '--summarize', action='store_true',
                            help='only information about the entered path')
    arg_parser.add_argument('-m', '--measure', action='store_true',
                            help='readable object sizes')
    arg_parser.add_argument('-t', '--tree', action='store_true',
                            help='view directory tree')
    arg_parser.add_argument('-d', '--depth', type=int, required=False, metavar='NUM', default=None,
                            help='analyzing objects up to a certain depth. Must be Positive')
    arg_parser.add_argument('-f', '--fullpath', action='store_true',
                            help='displaying full object paths')
    arg_parser.add_argument('--maxsize', type=int, required=False, metavar='NUM', default=None,
                            help='displaying NUM objects with maximum sizes. Must be Positive')
    arg_parser.add_argument('-w', '--window', action='store_true', required=False,
                            help='display in the window. '
                                 'Arrow keys for movement. '
                                 'Q or ESC to exit .')

    args = arg_parser.parse_args()

    if not os.path.isdir(args.path):
        print("Invalid argument path or directory not exist")
        exit(1)
    if args.depth is not None and args.depth <= 0:
        print("Invalid argument depth. Must be positive (from 1)")
        exit(2)
    if args.maxsize is not None and args.maxsize <= 0:
        print("Invalid argument maxsize. Must be positive (from 1)")
        exit(3)

    dirs_tree = DiskUsage(args.path).get_dirs_tree()

    if args.tree and args.maxsize is None:
        tree_view(dirs_tree, all=args.all, summarize=args.summarize, measure=args.measure, depth=args.depth,
                  fullpath=args.fullpath, window=args.window)
    else:
        list_view(dirs_tree, all=args.all, summarize=args.summarize, measure=args.measure, depth=args.depth,
                  fullpath=args.fullpath, max_count=args.maxsize, window=args.window)


if __name__ == '__main__':
    main()
