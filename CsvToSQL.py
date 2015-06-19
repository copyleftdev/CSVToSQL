import fnmatch
import os
import shutil
import csv
import sqlite3


def collectFiles(path, extention='csv'):
     matches = []

     for root, dirnames, filenames in os.walk(path):
         for filename in fnmatch.filter(filenames,'*.{}'.format(extention)):
             matches.append(os.path.join(root, filename))
     return matches


def CsvtoSqlite(dbloc):
    con = sqlite3.connect(dbloc)
    cur = con.cursor()
    files = collectFiles("data/")
    for eachFile in files:
        with open(eachFile,'rb') as fin:
            dr = csv.DictReader(fin)
            to_db = [(i['datetime'], i['host'],i['guid'],i['timings']) for i in dr]
            cur.executemany("INSERT INTO performance_runs (datetime, host, guid, timings) VALUES (?, ?, ?, ?);", to_db)
    con.commit()




def main():
    # print(collectFiles("data/"))
    CsvtoSqlite("db/performancedb.db")



if __name__ == '__main__':
    main()
