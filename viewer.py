from humanize import naturalsize


def view(files, measure=False, beautiful=False):
    if beautiful:
        pass
    else:
        show_normal_view(files, measure=measure)


def show_normal_view(files, measure=False):
    for file in files:
        if measure:
            print(f"{naturalsize(file.size):<30} {file.path}")
        else:
            print(f"{file.size:<30} {file.path}")


def show_beatiful_view(files, measure=False):
    for file in files:
        if measure:
            print(f"{naturalsize(file.size):<30} {file.path}")
        else:
            print(f"{file.size:<30} {file.path}")


def view_file_list(file_list):
    max_size_len = get_max_size_len(file_list)

    for file in file_list:
        print(f"{naturalsize(file.size):<30} {file.path}")


def get_max_size_len(files_list):
    max_size = 0
    for file in files_list:
        max_size = max(max_size, file.size)
    return max_size