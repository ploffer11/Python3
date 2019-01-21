import sys
import shutil
import zipfile
from pathlib import Path


class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        """
        # Attributes
        filename, search_string, replace_string, temp_directory """
        self.filename, self.search_string, self.replace_string, self.temp_directory = (
            filename, search_string, replace_string, Path(f"unzipped-{filename}")
        )
    
    def zip_find_replace(self):
        self.unzip_files() 
        self.find_replace()
        self.zip_files()

    def unzip_files(self):
        self.temp_directory.mkdir() # make folder named f"unzipped-{filename}"  
        with zipfile.ZipFile(self.filename) as zip: # make object zipfile.ZipFile(self.filename) and naming "zip"
            zip.extractall(self.temp_directory) # extract "zip" to temp_directory 
    
    def find_replace(self):
        for filename in self.temp_directory.iterdir(): # filename in temp_directory.iterdir()  
            with filename.open() as file: # open it
                contents = file.read() # read it
            contents = contents.replace(
                self.search_string, self.replace_string
            ) # replace search_string to replace_string in file
            with filename.open("w") as file: # open it mode "w"
                file.write(contents) # write it 
    
    def zip_files(self):
        with zipfile.ZipFile(self.filename, "w") as file: # open zipfile mode "w"
            for filename in self.temp_directory.iterdir(): # filename in temp_directory.iterdir()
                file.write(filename, filename.name) # write to zipfile filename -> filename.name, overwriting filename.name   
            shutil.rmtree(self.temp_directory)
    

#if __name__ == "__main__":
#    ZipReplace(*sys.argv[1:4]).zip_find_replace()

z = ZipReplace("test.zip", "천재", "바보")    
z.zip_find_replace()