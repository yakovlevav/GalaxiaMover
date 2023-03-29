import ftplib
 
HOSTNAME = "10.32.64.74"
USERNAME = "aoi"
PASSWORD = "Inspection@2023"


# Connect FTP Server
ftp_server = ftplib.FTP(HOSTNAME, USERNAME, PASSWORD)
ftp_server.dir()