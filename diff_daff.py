#! /bin/python3.11

"""Utility to diff .txt files"""

from difflib import HtmlDiff
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

test_file1 = '/home/ryan/PycharmProjects/diff_daff/test_text/jekyll_hyde_test_text1.txt'
test_file2 = '/home/ryan/PycharmProjects/diff_daff/test_text/jekyll_hyde_test_text2.txt'
file_timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


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


def html_diff(left_txt: str, right_txt: str, savedir: Path = Path.home() / "Downloads/") -> None:
    """
    Compares two given text files and saves a HTML document displaying the differences in the provided save directory.

    The HTML document uses different colors to show lines which are added, removed or changed. A legend detailing
    these color codes is placed at the top of the HTML file.

    Parameters
    ----------
    left_txt : str
        Path of the first file to refer for comparison.
    right_txt : str
        Path of the second file for comparison.
    savedir : Path, optional, default is current user's "Downloads" directory
        The directory where the resulting HTML file will be saved.

    Returns
    -------
    None
        This function doesn't return any value. It just saves an HTML report of the differences in
        two given files in the specified directory.

    """
    texts = get_diff_txt(left_txt, right_txt)
    save_path = Path(savedir).joinpath(f"diff_file_{file_timestamp}.html")
    html_diff_file = HtmlDiff().make_file(*texts)

    soup = BeautifulSoup(html_diff_file, 'html.parser')
    legend_table = soup.find_all('table')[1]
    soup.html.body.insert_before(legend_table)
    extract_table = soup.find_all('table')[2]
    soup.extract(extract_table)

    with open(save_path, "w") as file:
        file.write(str(soup))

if __name__ == '__main__':
    html_diff(test_file1, test_file2)
