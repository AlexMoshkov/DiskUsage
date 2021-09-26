import os
from file_info import FileInfo


class DiskUsage:
    def get_dirs_info(self, path, all=False, summarize=False):
        result = []

        if self.check_path(path):
            pass

        if summarize:
            size = self.get_size(path)
            return [FileInfo(size, path)]

        for dirpath, dirs, files in os.walk(path):
            if all:
                for file in files:
                    file_path = os.path.join(dirpath, file)
                    file_size = os.path.getsize(file_path)
                    result.append(FileInfo(file_size, file_path))

            size = self.get_size(dirpath)
            result.append(FileInfo(size, dirpath))
        return result[::-1]

    def get_size(self, start_path='.'):
        total_size = 0
        for dirpath, dirs, files in os.walk(start_path):
            for filename in files:
                file_path = os.path.join(dirpath, filename)
                if not os.path.islink(file_path):
                    total_size += os.path.getsize(file_path)
        return total_size

    def check_path(self, path):
        pass


if __name__ == '__main__':
    du = DiskUsage()
    result = du.get_dirs_info("C:\Games\Cyberpunk.2077.GOG.Rip-InsaneRamZes", summarize=True)
    print(*result)