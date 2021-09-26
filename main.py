import argparse

def main():
    arg_parser = argparse.ArgumentParser('DiskUsage')

    arg_parser.add_argument('-a', '--all', help='write counts for all files, not just directories')
    arg_parser.add_argument('-s', '--summarize', help='')

    args = arg_parser.parse_args()

    if args.all:
        pass
    if args.summarize:
        pass
