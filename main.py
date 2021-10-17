import argparse
from du import DiskUsage


def main():
    arg_parser = argparse.ArgumentParser('DiskUsage')

    arg_parser.add_argument('path', type=str, help='')
    arg_parser.add_argument('-a', '--all', action='store_true', help='write counts for all files, not just directories')
    arg_parser.add_argument('-s', '--summarize', action='store_true', help='')
    arg_parser.add_argument('-m', '--measure', action='store_true', help='')
    arg_parser.add_argument('-t', '--tree', action='store_true', help='')
    arg_parser.add_argument('-d', '--depth', nargs=1, type=int,
                            required=False, metavar=('depth',), help='', default=[None])
    arg_parser.add_argument('-f', '--fullpath', action='store_true', help='')

    args = arg_parser.parse_args()

    dirs_tree = DiskUsage(args.path).get_dirs_tree()

    if args.tree:
        dirs_tree.tree_view(all=args.all, summarize=args.summarize, measure=args.measure, depth=args.depth[0], fullpath=args.fullpath)
    else:
        dirs_tree.list_view(all=args.all, summarize=args.summarize, measure=args.measure, depth=args.depth[0], fullpath=args.fullpath)


if __name__ == '__main__':
    main()

# TODO: сделать ключ -m <число> для отображения самых жирных директорий (которые не имеют поддиректорий) (при ключе -a файлов)
# TODO: сделать ключ -w для отображения в окне типо как в виме