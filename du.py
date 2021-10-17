import os
from file import FileInfo
from directory import Directory


class DiskUsage:
    def __init__(self, path):
        self.root = path

    def get_dirs_tree(self):
        size = self._get_size(self.root)
        root_dir = Directory(self.root, size, [], [], 0)
        self._get_subdirs(root_dir, 0)
        return root_dir

    def _get_subdirs(self, dir, depth, all=False, summarize=False):
        contents = os.listdir(dir.path)
        for content in contents:
            sub_path = os.path.join(dir.path, content)

            if os.path.isdir(sub_path):
                sub_size = self._get_size(sub_path)
                subdir = Directory(sub_path, sub_size, [], [], depth + 1)
                self._get_subdirs(subdir, depth + 1, all=all, summarize=summarize)
                dir.subdirs.append(subdir)
            else:
                sub_size = os.path.getsize(sub_path)
                file = FileInfo(sub_path, sub_size, depth + 1)
                dir.files.append(file)

    def _get_size(self, start_path='.'):
        total_size = 0
        for dirpath, dirs, files in os.walk(start_path):
            for filename in files:
                file_path = os.path.join(dirpath, filename)
                if not os.path.islink(file_path):
                    total_size += os.path.getsize(file_path)
        return total_size

    def _check_path(self, path):
        pass
