import ftplib
from glob import glob
import os

class galaxiamover:
    def __init__(self):
        self.hostname = "10.32.64.74"
        self.username = "aoi"
        self.password = "Inspection@2023"
        
    def open_connection(self):
        ftp_server = ftplib.FTP(self.hostname, self.username, self.password)
        
    def get_files_to_transfer(self, path_to_the_file):
        glob_input = os.path.join(path_to_the_file,"*.xml")
        filelist = glob(glob_input)
        return(filelist)
        

gl = galaxiamover()
print(gl.get_files_to_transfer('Data'))
