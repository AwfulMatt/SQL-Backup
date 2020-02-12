import time
import datetime
import os

from time import sleep

db_host = 'localhost'
db_user = 'username'
db_password = 'yourpassword'

backup_path = 'G:\\Backups'
backup_time = 120 # Minutes

databases = ["database1", "database2"]

datetime = time.strftime('%Y-%m-%d-%H-%M-%S')
os.system("cls")
while True:
    for db in databases:
        filename = "%s%s.sql" % (db, datetime)

        if db_password != '':
            dump = "mysqldump -h %s -u %s -p %s %s > %s\\%s" % (db_host, db_user, db_password, db, backup_path, filename)
        else:
            dump = "mysqldump -h %s -u %s %s > %s\\%s" % (db_host, db_user, db, backup_path, filename)

        os.system(dump)
        print("Database %s has been backed up to %s." % (db, backup_path))
    sleep(backup_time * 60)
