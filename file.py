from humanize import naturalsize


class FileInfo:
    def __init__(self, path, size, depth):
        self.path = path
        self.size = size
        self.depth = depth

    def print(self, measure=False):
        size = self.size
        if measure:
            size = naturalsize(size)
        print(f"{size:<20} {self.path}")

    def get_normalize_size(self):
        return naturalsize(self.size)
