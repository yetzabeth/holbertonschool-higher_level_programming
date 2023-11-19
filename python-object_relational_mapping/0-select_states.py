#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import sys
import MySQLdb
if __name__ == "__main__":
    # take args from the promp
    arg = sys.argv
    DB_HOST = 'localhost'
    DB_USER = arg[1]
    DB_PASS = arg[2]
    DB_NAME = arg[3]

    data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    # connect to db
    conn = MySQLdb.connect(*data)

    # create cursor
    cursor = conn.cursor()

    # exe query
    query = 'SELECT * FROM states ORDER BY id ASC'
    cursor.execute(query)

    # Fetch the results of a select
    res = cursor.fetchall()

    # print response
    for i in res:
        print(i)
