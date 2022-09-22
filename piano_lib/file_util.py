import datetime
import csv
import os
import glob


def readlines(file_name="intervals.csv"):
    with open(file_name) as debts:
        return debts.readlines()


def cleanFolder():
    output = glob.glob('out/*.csv')
    print("deleting: ")
    print(output)
    for filename in output:
        os.remove(filename)


def load_file_as_string(file_name):
    with open(file_name) as sqlfile:
        return ''.join(sqlfile.readlines())


def save(content, mode="wt", name="data", random=datetime.datetime.today().strftime("%Y%m%d%H%M%S")):
    file_name = "-" + name + ".csv"
    with open(file_name, mode) as save_file:
        datawriter = csv.writer(save_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        datawriter.writerows(content)


def save_append(content, mode="a", name="data", random=datetime.datetime.today().strftime("%Y%m%d%H%M%S")):
    file_name = "./out/" + name + ".csv"
    with open(file_name, mode) as save_file:
        datawriter = csv.writer(save_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        datawriter.writerows(content)
