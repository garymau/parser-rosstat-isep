import pytest
from pathlib import Path

from getter import *

YEAR, MONTH = 2017, 10
PUB = '1-0'
URL = 'http://www.gks.ru/bgd/free/B17_00/IssWWW.exe/Stg/dk10/'f'{PUB}.doc'
ROOT = Path(__file__).parent.parent
assert ROOT.name == "parser-rosstat-isep"

PATH = ROOT / 'data/2017/10/raw/'f'{PUB}.doc'


def test_download():
    if PATH.exists():
        PATH.unlink()
    download(URL, PATH)
    assert PATH.exists() and PATH.is_file()


def test_url():
    result = url(YEAR, MONTH, PUB)
    assert result == URL


class TestFolder:
    f = Folder(YEAR, MONTH)

    def test_folder_on_init_sets_path(self):
        path = ROOT / 'data' / str(YEAR) / str(MONTH)
        assert path == self.f.path

    def test_mkdir_on_given_path_creates_directory(self):
        dir = PATH.parent
        Folder.md(dir)
        assert dir.exists() and dir.is_dir()

    def test_interim_property(self):
        assert self.f.interim.exists() and self.f.interim.is_dir()

    def test_raw_property(self):
        assert self.f.raw.exists() and self.f.raw.is_dir()

    def test_subfolder(self):
        assert callable(self.f.subfolder)


class TestDocFile:
    doc = DocFile(YEAR, MONTH, PUB)

    def test_url_on_init_is_valid(self):
        assert self.doc.url == URL

    def test_path_on_init_is_valid(self):
        assert self.doc.path == PATH

    def test_size_property(self):
        file_size = int(round(PATH.stat().st_size / 1024, 0))
        assert self.doc.size == file_size

    def test_download(self):
        assert callable(self.doc.download)

    def test_to_csv(self):
        assert callable(self.doc.to_csv)


class TestInterimCSV:
    target = 'main'
    icsv = InterimCSV(YEAR, MONTH, target)

    def test_interim_csv_on_init_creates_path_to_csv_file(self):
        path = PATH.parents[1] / 'interim' / f'{self.target}.csv'
        assert self.icsv.path == path

    def test_from_csv_(self):
        assert callable(self.icsv.from_csv)


class TestFile:

    def test_target_on_init_is_defined(self):
        target = 'main'
        f = File(YEAR, MONTH, target)
        assert f.target == target

    def test_postfix_on_target_in_stable_file_section(self):
        m = MONTH
        target = 'main'
        f = File(YEAR, m, target)
        assert f.target in f.stable_files.keys() and f.postfix == f.stable_files[target][0]

    def test_postfix_on_target_in_section2_a(self):
        m = MONTH
        target = 'pwr'
        f = File(YEAR, m, target)
        assert f.target in f.section2_a.keys() and f.postfix == f.section2_a[target][0]

    def test_postfix_on_target_in_section2_b(self):
        m = 5
        target = 'ip'
        f = File(YEAR, m, target)
        assert f.target in f.section2_b.keys() and f.postfix == f.section2_b[target][0]

    def test_download(self):
        assert callable(File.download)

    def test_to_csv(self):
        assert callable(File.download)

    def test_from_csv(self):
        assert callable(File.download)


def test_official_dates():
    dates = []
    for y, m in official_dates():
        dates.append((y, m))
    assert dates == [(2016, 1), (2016, 2), (2016, 3), (2016, 4),
                     (2016, 5), (2016, 6), (2016, 7), (2016, 8),
                     (2016, 9), (2016, 10), (2016, 11), (2016, 12),
                     (2017, 1), (2017, 2), (2017, 3), (2017, 4),
                     (2017, 5), (2017, 6), (2017, 7), (2017, 8),
                     (2017, 9), (2017, 10)]


if __name__ == "__main__":
    pytest.main([__file__])
