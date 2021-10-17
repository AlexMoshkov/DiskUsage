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

    def walk(self, all=False):
        yield self
        if all:
            for file in self.files:
                yield file
        for subdir in self.subdirs:
            yield from subdir.walk(all=all)

    def list_view(self, all=False, summarize=False, measure=False, depth=None, fullpath=False):
        root = None if fullpath else self.path
        print(depth)
        if summarize:
            self.print(measure=measure)
            return
        reversed_walk = list(self.walk(all=all))[::-1]
        for obj in reversed_walk:
            if depth is None or obj.depth <= depth:
                obj.print(measure=measure, root_path=root)

    def tree_view(self, all=False, summarize=False, measure=False, depth=None, fullpath=False):
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
                content_name = content.path if fullpath else content.name
                yield f"{prefix}{pointer}[{size}] {content_name}"
                if isinstance(content, Directory):
                    extension = branch if pointer == tee else space
                    if depth is None or content.depth < depth:
                        yield from tree_lines(content, prefix=prefix + extension)
        print(f"[{naturalsize(self.size) if measure else self.size}]")
        for line in tree_lines(self):
            print(line)

    def print(self, measure=False, root_path=None):
        size = naturalsize(self.size) if measure else self.size
        path = self.path if root_path is None else os.path.relpath(self.path, root_path)
        print(f"{size:<20} {path}")


# TODO: реализовать возможность игнора скрытых директорий и файлов
