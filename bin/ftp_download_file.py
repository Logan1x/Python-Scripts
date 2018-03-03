import argparse
import os
from ftplib import FTP


def parse_args():
    ''' parse and check command line arguments '''
    ap = argparse.ArgumentParser(description="FTP Utility")
    ap.add_argument('-hh', dest='host', help="Host name")
    ap.add_argument('-u', dest='username', help="user name")
    ap.add_argument('-p', dest='password', help="user password")
    ap.add_argument('-rd', dest='remote_dir', help="Path to remote directory")
    ap.add_argument('-ld', dest='local_dir', help="Path to local directory")
    ap.add_argument(dest='files', help="File names", nargs='+')
    return ap.parse_args()


def is_empty(file):
    file_size = os.stat(file).st_size
    if file_size == 0:
        print('The file {} is empty'.format(file))
        return True
    return False


args = parse_args()

host = args.host
username = args.username
password = args.password
remote_dir = args.remote_dir
local_dir = args.local_dir
files = args.files

ftp = FTP(host)
ftp.login(username, password)
ftp.cwd(remote_dir)

for file in files:
    try:
        local_filename = os.path.join(local_dir, file)
        print('Getting filename: ' + file)
        ftp.retrbinary('RETR %s' % file, open(local_filename, 'wb').write)
        print('Saving at %s' % local_filename)
    except Exception as err:
        print(err)
        if (is_empty(local_filename)):
            os.remove(local_filename)
        continue

ftp.quit()
