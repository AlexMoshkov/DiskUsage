from humanize import naturalsize
import os


class DirectoryInfo:
    def __init__(self, path, size, subdirs, files, depth):
        self.path = path
        self.size = size
        self.subdirs = subdirs
        self.files = files
        self.depth = depth

    @property
    def name(self):
        return os.path.basename(self.path)

    def walk(self, all=False):
        yield self
        if all:
            for file in self.files:
                yield file
        for subdir in self.subdirs:
            yield from subdir.walk(all=all)

    def files_walk(self):
        for file in self.files:
            yield file
        for subdir in self.subdirs:
            yield from subdir.files_walk()

    def get_max_objects(self, count, files=False):
        if files:
            array = list(self.files_walk())
        else:
            array = list(filter(lambda x: len(x.subdirs) == 0, self.walk()))
        array.sort(key=lambda x: x.size, reverse=True)
        return array[:count]

    def str(self, measure=False, root_path=None):
        size = naturalsize(self.size) if measure else self.size
        path = self.path if root_path is None else os.path.relpath(self.path, root_path)
        return f"{size:<20} {path}"
