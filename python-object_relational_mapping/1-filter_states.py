#!/usr/bin/python3
""" lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa """

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
    query = "SELECT * FROM states WHERE name"
    query_part_two = "LIKE BINARY 'N%' ORDER BY states.id ASC"

    cursor.execute(f'{query} {query_part_two}')

    # Fetch the results of a select
    res = cursor.fetchall()

    # print response
    for i in res:
        print(i)
