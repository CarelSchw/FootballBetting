import sys
import pandas as pd
import pymysql
import os
import numpy as np

# query for date:
# update matches
# set matches.Date = date_format(STR_TO_DATE(Date, '%m/%d/%y'), '%y-%m-%d');

directory = "Matches/"

mydb = pymysql.connect(host="37.128.146.217", user="knar", password="knarknar", db="betting_with_knar")
cursor = mydb.cursor()

for file in os.listdir(directory):
    print('Matches/'+file)
    csv_data = pd.read_csv("Matches/" + file)
    for row in csv_data.iterrows():
        list = row[1].values
        list[5] = list[5].replace("'", "")
        list[6] = list[6].replace("'", "")
        # print(tuple(list))
        # print(len(list))
        # if len(list) == 65:
        #     list = np.append(list[:10], list[11:])
        series = pd.Series(list)
        if not series.isnull().values.any():
            cursor.execute(
                "INSERT INTO low_data_matches VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%d', '%d', '%s', '%f',"
                " '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f');" % tuple(list))




# close the connection to the database.
mydb.commit()
cursor.close()
mydb.close()
print("Done")

# Cursor for table with length of 64:
# cursor.execute("INSERT INTO matches VALUES('%s', '%s', '%s', '%s', '%d', '%d', '%s', '%d', '%d', '%s', '%d',"
#                            " '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%d', '%f', '%f', '%f', '%f', '%f',"
#                            " '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f', '%f',"
#                            " '%d', '%f', '%f', '%f', '%f', '%f', '%f', '%d', '%f', '%f', '%f', '%f', '%d', '%f', '%f', '%f',"
#                            " '%f', '%f', '%f', '%f', '%f');" % tuple(list))