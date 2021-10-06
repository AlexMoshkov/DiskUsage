import os
from humanize import naturalsize


class Directory:
    def __init__(self, path, size, subdirs, files, depth):
        self.path = path
        self.size = size
        self.subdirs = subdirs
        self.files = files
        self.depth = depth

    def walk(self):
        yield self
        for subdir in self.subdirs:
            yield from subdir.walk()

    def list_view(self, all=False, summarize=False):
        reversed_walk = list(self.walk())[::-1]
        for dir in reversed_walk:
            print(dir)

    def tree_view(self, all=False):
        pass

    def __str__(self):
        return f"{self.size:<40} {self.path}"


# TODO: геттер для dir_name
# TODO: реализовать возможность игнора скрытых директорий и файлов