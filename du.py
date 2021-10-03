import os
from file_info import FileInfo


class DiskUsage:
    def get_dirs_info(self, path, all=False, summarize=False):
        result = []

        if self.check_path(path):
            pass

        if summarize:
            size = self.get_size(path)
            return [FileInfo(size, path, 0)]

        for root, dirs, files in os.walk(path):
            depth = root.replace(path, '').count(os.sep)
            size = self.get_size(root)
            result.append(FileInfo(size, os.path.relpath(root, path), depth))

            if all:
                for file in files:
                    file_path = os.path.join(root, file)
                    file_depth = file_path.replace(path, '').count(os.sep)
                    file_size = os.path.getsize(file_path)
                    result.append(FileInfo(file_size, os.path.relpath(file_path, path), file_depth))
        return result[::-1]

    def get_size(self, start_path='.'):
        total_size = 0
        for dirpath, dirs, files in os.walk(start_path):
            for filename in files:
                file_path = os.path.join(dirpath, filename)
                if not os.path.islink(file_path):
                    total_size += os.path.getsize(file_path)
        return total_size

    def check_path(self, path):
        pass
