import fnmatch
import os
import shutil
import csv
import sqlite3


def collectFiles(path, tmpdest, extention='csv'):
     matches = []

     for root, dirnames, filenames in os.walk(path):
         for filename in fnmatch.filter(filenames,'*.{}'.format(extention)):
             matches.append(os.path.join(root, filename))

     for eachMatchedItem in matches:
         shutil.copy(eachMatchedItem,tmpdest)


def CvstoSqlite(csvloc, dbloc):
    cvsfileList = os.listdir(csvloc)

    conn = sqlite3.connect(dbloc)
    cur = conn.cursor()

    for csvFile in cvsfileList:
        with open("{}{}".format(csvloc, csvFile),'rb') as csvout:
            dr = csv.DictReader(csvout)
            to_sqlite = [(i['datetime'],i['host'],i['guid'],i['timings']) for i in dr]
        cur.executemany("INSERT INTO performance_runs (datetime, host, guid, timings) VALUES (?, ?, ?, ?);", to_sqlite)
        con.commit()




def main():
    collectFiles("data/","temp/")
    CvstoSqlite("temp/","db/performancedb.db")



if __name__ == '__main__':
    main()
