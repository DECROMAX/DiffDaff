from difflib import Differ
from pathlib import Path

test_file1 = '/home/ryan/PycharmProjects/diff_daff/test_text/jekyll_hyde_test_text1.txt'
test_file2 = '/home/ryan/PycharmProjects/diff_daff/test_text/jekyll_hyde_test_text1.txt'


def get_diff_txt(filepath1: str, filepath2: str) -> tuple[list[str], list[str]]:
    """:arg 2 * string file paths of text files to diff, :returns tuple of str"""

    # check if file exists
    try:
        file1 = Path(filepath1)
        file2 = Path(filepath2)
    except (FileNotFoundError | FileExistsError) as e:
        raise e(f"Filepath error: {e}")

    # check if txt file, return txt

    if file1.suffix != ".txt":
        raise ValueError(f"{file1} is not a .txt file")
    elif file2.suffix != ".txt":
        raise ValueError(f"{file2} is not a txt file")
    else:
        with (
            open(file1) as txt_file1,
            open(file2) as txt_file2,
        ):
            return txt_file1.readlines(), txt_file2.readlines()


