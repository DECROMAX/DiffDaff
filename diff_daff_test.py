import unittest
from pathlib import Path
from diff_daff import get_diff_txt


class TestDiffDaff(unittest.TestCase):
    def test_get_diff_txt(self):
        filepath1 = "/home/ryan/PycharmProjects/diff_daff/test_text/jekyll_hyde_test_text1.txt"
        filepath2 = "/home/ryan/PycharmProjects/diff_daff/test_text/jekyll_hyde_test_text2.txt"

        # Make sure that testing files exist before running this test
        file1 = Path(filepath1)
        file2 = Path(filepath2)

        self.assertTrue(file1.exists(), f"'{filepath1}' does not exist.")
        self.assertTrue(file2.exists(), f"'{filepath2}' does not exist.")

        # Here, place your logic to test 'get_diff_txt'
        # Replace 'expected_output' with the actual expected output
        expected_output = (['line1 from file1', 'line2 from file1'], ['line1 from file2', 'line2 from file2'])
        self.assertEqual(get_diff_txt(filepath1, filepath2), expected_output)


if __name__ == "__main__":
    unittest.main()
