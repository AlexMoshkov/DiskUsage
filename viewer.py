from du import DiskUsage


def view_file_list(file_list):
    for file in file_list:
        print(file)


def get_max_size(files_list):
    max_size = 0
    for file in files_list:
        max_size = max(max_size, file.size)
    return max_size