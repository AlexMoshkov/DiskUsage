import os
from humanize import naturalsize
from subprocess import run


class ObjectInfo:
    def __init__(self, size, path):
        self.size = size
        self.path = path


class DiskUsage:
    def __init__(self):
        pass

    def get_dirs_info(self, path):
        result = []

        if self.check_path(path):
            pass
        print(self.get_size(path), path)
        #process = run(['du', '-sh', path], capture_output=True, text=True)
        #print(process.stdout.split()[0], path)

    def get_size(self, start_path='.'):
        total_size = 0
        for dirpath, dirs, files in os.walk(start_path):
            for filename in files:
                file_path = os.path.join(dirpath, filename)
                total_size += os.stat(file_path).st_size
        return total_size

    def check_path(self, path):
        pass


if __name__ == '__main__':
    du = DiskUsage()
    du.get_dirs_info("/home/alex/PycharmProjects")