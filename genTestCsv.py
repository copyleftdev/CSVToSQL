#Generate test csv files
import random
import os
from faker import Factory


fake = Factory.create()

def generateCsvFile(path, filename, recordCount):


    with open("{}{}.csv".format(path, filename),"w") as csvFile:
        csvFile.write("datetime,host,guid,timings\n")
        for i in range(recordCount):
            dataSeed = '"{}","{}","{}","{}"\n'.format(fake.date_time(),
                                                           fake.ipv4(),
                                                           fake.uuid4(),
                                                           random.uniform(0.5,8.0))
            csvFile.write(dataSeed)


generateCsvFile("data/TEST_02/1/","firstlevel",4000)
