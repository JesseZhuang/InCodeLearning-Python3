from unittest import TestCase

from algorithm.ood import cloud_storage


class TestCloudStorage(TestCase):
    def test_level1(self):
        queries = [
            ["ADD_FILE", "/dir1/dir2/file.txt", "10"],
            ["ADD_FILE", "/dir1/dir2/file.txt", "5"],
            ["GET_FILE_SIZE", "/dir1/dir2/file.txt"],
            ["DELETE_FILE", "/non-existing.file"],
            ["DELETE_FILE", "/dir1/dir2/file.txt"],
            ["GET_FILE_SIZE", "/not-existing.file"]
        ]
        exp = [
            "true",  # adds file
            "false",  # already exists
            "10",
            "",  # file not found
            "10",
            ""
        ]
        self.assertEqual(cloud_storage.solution(queries), exp)

    def test_level2(self):
        queries = [
            ["ADD_FILE", "/dir/file1.txt", "5"],
            ["ADD_FILE", "/dir/file2", "20"],
            ["ADD_FILE", "/dir/deeper /file3.mov", "9"],
            ["GET_N_LARGEST", "/dir", "2"],
            ["GET_N_LARGEST", "/dir/file", "3"],
            ["GET_N_LARGEST", "/another_dir", "file.txt"],
            ["ADD_FILE", "/big_file.mp4", "20"],
            ["GET_N_LARGEST", "/", "2"]
        ]
        exp = [
            "true",
            "true",
            "true",
            "/dir/file2(20), /dir/deeper/file3.mov(9)",
            "/dir/file2(20), /dir/file1.txt(5)",
            "",  # no files with that prefix /another_dir
            "true",
            "/big_file.mp4(20), /dir/file2(20)"
        ]

    def test_level3(self):
        queries = [
            ["ADD_USER", "user1", "200"],
            ["ADD_USER", "user1", "100"],
            ["ADD_FILE_BY", "user1", "/dir/file.med", "50"],
            ["ADD_FILE_BY", "user1", "/file.big", "140"],
            ["ADD_FILE_BY", "user1", "/dir/file.small", "20"],
            ["ADD_FILE", "/dir/admin_file", "300"],
            ["ADD_USER", "user2", "110"],
            ["ADD_FILE_BY", "user2", "/dir/file.med", "45"],
            ["ADD_FILE_BY", "user2", "/new_file", "50"],
            ["MERGE_USER", "user1", "user2"]
        ]
        exp = [
            "true",
            "false",
            "150",
            "10",
            "",
            "true",  # admin unlimited capacity
            "true",
            "",
            "60",
            "70",
        ]
