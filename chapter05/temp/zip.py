import shutil
import sys
import zipfile
from pathlib import Path

from PIL import Image


class ZipProcessor:
    def __init__(self, zipname):
        self.zipname = zipname
        self.temp_directory = Path("unzipped-{}".format(zipname[:-4]))

    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            # 将提取的文件放入temp_directory目录中
            zip.extractall(str(self.temp_directory))

    def zip_files(self):
        with zipfile.ZipFile(self.zipname, 'w') as file:
            for filename in self.temp_directory.iterdir():
                # print("param1 = {}, param2 = {}", str(filename), filename.name)
                # 将临时目录中的文件内容，写入zip包的对应文件中
                file.write(str(filename), filename.name)
        # 删除目录
        shutil.rmtree(str(self.temp_directory))

    def process_files(self):
        pass


class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string = search_string
        self.replace_string = replace_string

    def process_files(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(self.search_string, self.replace_string)
            with filename.open("w") as file:
                file.write(contents)


class ScaleZip(ZipProcessor):
    def process_files(self):
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            print(str(filename))

            scaled = im.resize((640, 480))
            scaled.save(str(filename))


if __name__ == "__main__":
    # ZipReplace(*sys.argv[1:4]).process_zip()
    ScaleZip(*sys.argv[1:4]).process_zip()
