class FileInfo:
    def __init__(self, size, path):
        self.size = size
        self.path = path

    def __str__(self):
        return f"{self.size} {self.path}\n"
