import os
import pytest
import du
from directory import DirectoryInfo


class TestDiskUsage:
    @staticmethod
    def setup():
        if "TestDir" in os.listdir():
            return
        dir = os.path.curdir
        dir = os.path.join(dir, "TestDir")
        os.mkdir(dir)
        os.mkdir(os.path.join(dir, "AnotherTestDir"))
        open(os.path.join(dir, 'testfile.txt'), 'w').close()
        os.mkdir(os.path.join(dir, "AnotherTestDir/testdir"))

    def test_dirs_tree(self):
        path = os.path.join(os.path.curdir, "TestDir")
        diskUsage = du.DiskUsage(path)
        dirs_tree = diskUsage.get_dirs_tree()
        assert isinstance(dirs_tree, DirectoryInfo)
        assert dirs_tree.path == path
        assert dirs_tree.depth == 0
        assert len(dirs_tree.files) == 1
        assert len(dirs_tree.subdirs) == 1
