from humanize import naturalsize
from directory import DirectoryInfo


def list_view(dir, all=False, summarize=False, measure=False, depth=None, fullpath=False, max_count=None):
    root = None if fullpath else dir.path
    if summarize:
        dir.print(measure=measure)
        return

    if max_count is None:
        walk = list(dir.walk(all=all))[::-1]
    else:
        walk = dir.get_max_objects(max_count, files=all)

    for obj in walk:
        if depth is None or obj.depth <= depth:
            obj.print(measure=measure, root_path=root)


def tree_view(dir, all=False, summarize=False, measure=False, depth=None, fullpath=False):
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
            if isinstance(content, DirectoryInfo):
                extension = branch if pointer == tee else space
                if depth is None or content.depth < depth:
                    yield from tree_lines(content, prefix=prefix + extension)
    print(f"[{naturalsize(dir.size) if measure else dir.size}]")
    if not summarize:
        for line in tree_lines(dir):
            print(line)
