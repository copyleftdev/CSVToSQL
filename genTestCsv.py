#Generate test csv files
import random
import os
import string
from faker import Factory
import subprocess

fake = Factory.create()

def generateCsvFile(path, filename, recordCount):


    with open("{}{}.csv".format(path, filename),"w") as csvFile:
        for i in range(recordCount):
            dataSeed = '"{}","{}","{}","{}"\n'.format(fake.date_time(),
                                                           fake.ipv4(),
                                                           fake.uuid4(),
                                                           random.uniform(0.5,8.0))
            csvFile.write(dataSeed)
