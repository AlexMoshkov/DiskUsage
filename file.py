from humanize import naturalsize
import os


class FileInfo:
    def __init__(self, path, size, depth):
        self.path = path
        self.size = size
        self.depth = depth

    @property
    def name(self):
        return os.path.basename(self.path)

    def str(self, measure=False, root_path=None):
        size = naturalsize(self.size) if measure else self.size
        path = self.path if root_path is None else os.path.relpath(self.path, root_path)
        return f"{size:<20} {path}"
