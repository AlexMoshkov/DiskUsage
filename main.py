import argparse
from du import DiskUsage
from viewer import view


def main():
    arg_parser = argparse.ArgumentParser('DiskUsage')

    arg_parser.add_argument('path', type=str, help='')
    arg_parser.add_argument('-a', '--all', action='store_true', help='write counts for all files, not just directories')
    arg_parser.add_argument('-s', '--summarize', action='store_true', help='')
    arg_parser.add_argument('-m', '--measure', action='store_true', help='') #
    arg_parser.add_argument('-b', '--beautiful', action='store_true', help='') #

    args = arg_parser.parse_args()

    result = DiskUsage().get_dirs_info(args.path, all=args.all, summarize=args.summarize)
    view(result, measure=args.measure)


if __name__ == '__main__':
    main()