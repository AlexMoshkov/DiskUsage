import argparse
from du import DiskUsage
from viewer import view_file_list


def main():
    arg_parser = argparse.ArgumentParser('DiskUsage')

    arg_parser.add_argument('path', type=str, help='')
    arg_parser.add_argument('-a', '--all', help='write counts for all files, not just directories')
    arg_parser.add_argument('-s', '--summarize', help='')

    args = arg_parser.parse_args()

    print(args.path)
    result = DiskUsage().get_dirs_info(args.path, all=args.all, summarize=args.summarize)
    view_file_list(result)


if __name__ == '__main__':
    main()