from humanize import naturalsize
import os


class Directory:
    def __init__(self, path, size, subdirs, files, depth):
        self.path = path
        self.size = size
        self.subdirs = subdirs
        self.files = files
        self.depth = depth

    @property
    def name(self):
        return os.path.basename(self.path)

    def walk(self):
        yield self
        for subdir in self.subdirs:
            yield from subdir.walk()

    def list_view(self, all=False, summarize=False, measure=False, depth=None):
        print(depth)
        if summarize:
            self.print(measure=measure)
            return
        reversed_walk = list(self.walk())[::-1]
        for dir in reversed_walk:
            if depth is None or dir.depth <= depth:
                dir.print(measure=measure)
            if all:
                for file in dir.files:
                    if depth is None or file.depth <= depth:
                        file.print(measure=measure)

    def tree_view(self, all=False, summarize=False, measure=False, depth=None):
        space = '    '
        branch = '│   '
        tee = '├── '
        last = '└── '

        def tree_lines(dir, prefix=''):
            contents = dir.subdirs
            if all:
                contents += dir.files
            pointers = [tee] * (len(contents) - 1) + [last]
            for pointer, content in zip(pointers, contents):
                size = str(naturalsize(content.size) if measure else content.size)
                yield f"{prefix}{pointer}[{size}] {content.name}"
                if isinstance(content, Directory):
                    extension = branch if pointer == tee else space
                    if depth is None or content.depth < depth:
                        yield from tree_lines(content, prefix=prefix + extension)
        print(f"[{naturalsize(self.size) if measure else self.size}]")
        for line in tree_lines(self):
            print(line)

    def print(self, measure=False):
        size = self.size
        if measure:
            size = naturalsize(self.size)
        print(f"{size:<20} {self.path}")


# TODO: реализовать возможность игнора скрытых директорий и файлов
