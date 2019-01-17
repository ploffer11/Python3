import sys
import shutil
import zipfile
from pathlib import Pathx
from PIL import Image

class ZipProcessor:
    def __init__(self, zipname):
        self.zipname, self.temp_directory = (
            zipname, Path(f"unzipped-{zipname[:-4]}")
        )
    
    def process_zip(self):
        self.unzip_files()
        self.process_files()
        self.zip_files()
    
    def unzip_files(self):
        self.temp_directory.mkdir()
        with zipfile.ZipFile(self.zipname) as zip:
            zip.extractall(self.temp_directory)
    
    def zip_files(self):
        with zipfile.ZipFile(self.zipname, "w") as file:
            for filename in self.temp_directory.iterdir():
                file.write(filename, filename.name)
        shutil.rmtree(self.temp_directory)
    
class ZipReplace(ZipProcessor):
    def __init__(self, filename, search_string, replace_string):
        super().__init__(filename)
        self.search_string, self.replace_string = (
            search_string, replace_string
        )
    
    def process_files(self):
        for filename in self.temp_directory.iterdir():
            with filename.open() as file:
                contents = file.read()
            contents = contents.replace(
                self.search_string, self.replace_string
            )
            with filename.open("w") as file:
                file.write(contents)

class ScaleZip(ZipProcessor):
    def process_files(self):
        for filename in self.temp_directory.iterdir():
            im = Image.open(str(filename))
            scaled = im.resize((640, 480))
            scaled.save(filename)

