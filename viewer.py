from du import DiskUsage


def view(path, all=False, summarize=False):
    du = DiskUsage()
    files_list = du.get_dirs_info(path)

    max_lenght = len(str(get_max_size()))

    for file in files_list:
        print(file)

def get_max_size(files_list):
    max_size = 0
    for file in files_list:
        max_size = max(max_size, file.size)
    return max_size