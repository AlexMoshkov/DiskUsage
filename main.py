import argparse
from du import DiskUsage


def main():
    arg_parser = argparse.ArgumentParser('DiskUsage')

    arg_parser.add_argument('path', type=str, help='')
    arg_parser.add_argument('-a', '--all', action='store_true', help='write counts for all files, not just directories')
    arg_parser.add_argument('-s', '--summarize', action='store_true', help='')
    arg_parser.add_argument('-m', '--measure', action='store_true', help='') #
    arg_parser.add_argument('-b', '--beautiful', action='store_true', help='') #

    args = arg_parser.parse_args()

    dirs_tree = DiskUsage(args.path).get_dirs_tree()
    dirs_tree.list_view()


if __name__ == '__main__':
    main()
