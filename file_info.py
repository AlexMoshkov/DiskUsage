from humanize import naturalsize

class FileInfo:
    def __init__(self, size, path, depth):
        self.size = size
        self.path = path
        self.depth = depth

    def __str__(self):
        return f"{self.size:<20} {self.path} {self.depth}"

    def get_natural_size(self):
        return naturalsize(self.size)
