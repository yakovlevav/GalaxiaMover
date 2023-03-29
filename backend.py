import ftplib
from glob import glob
import os
os.path.sep = "/"

class galaxiamover:
    def __init__(self):
        self.hostname = "10.32.64.74"
        self.username = "aoi"
        self.password = "Inspection@2023"
        self.work_directory = '/'.join( ('AOI_Production', 'AOI_Output') )
        
    def open_connection(self):
        self.ftp_server = ftplib.FTP(self.hostname, self.username, self.password)
        self.ftp_server.cwd(self.work_directory)
        
    def close_connection(self):
        self.ftp_server.quit()
        
    def send_file(self, file_path):
        filename = os.path.basename(file_path)
        print(filename)
        print(self.ftp_server.pwd())
        with open(file_path, 'rb') as file:
            self.ftp_server.storbinary('STOR {}'.format( filename ), fp=file)
        
    def get_files_to_transfer(self, path_to_the_file):
        glob_input = os.path.join(path_to_the_file,"*.xml")
        filelist = glob(glob_input)
        return(filelist)
        
gl = galaxiamover()
file = gl.get_files_to_transfer('Data')
gl.open_connection()
gl.send_file(file[0])
gl.close_connection()
