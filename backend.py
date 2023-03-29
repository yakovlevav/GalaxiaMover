import ftplib
from glob import glob
import os
import watchdog.events
import watchdog.observers
import time

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
        with open(file_path, 'rb') as file:
            self.ftp_server.storbinary('STOR {}'.format( filename ), fp=file)
        
    def get_files_to_transfer(self, path_to_the_file):
        glob_input = os.path.join(path_to_the_file,"*.xml")
        filelist = glob(glob_input)
        return(filelist)
    
    def push_list_of_files(self):
        return()
    
    
class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.xml'],
                                                             ignore_directories=True, case_sensitive=False)
 
    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)
        
if __name__ == "__main__":
    # gl = galaxiamover()
    # file = gl.get_files_to_transfer('Data')
    # gl.open_connection()
    # gl.send_file(file[0])
    # gl.close_connection()
    
    src_path = 'Data'
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()