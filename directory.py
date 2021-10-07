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

    def list_view(self, all=False, summarize=False, measure=False):
        if summarize:
            self.print(measure=measure)
            return
        reversed_walk = list(self.walk())[::-1]
        for dir in reversed_walk:
            dir.print(measure=measure)
            if all:
                for file in dir.files:
                    file.print(measure=measure)

    def tree_view(self, all=False, summarize=False):
        pass

    def print(self, measure=False):
        size = self.size
        if measure:
            size = naturalsize(self.size)
        print(f"{size:<20} {self.path}")


# TODO: геттер для dir_name
# TODO: реализовать возможность игнора скрытых директорий и файлов
