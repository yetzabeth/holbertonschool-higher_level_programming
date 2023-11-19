#!/usr/bin/python3
""" Filter states by user input """

import sys
import MySQLdb
if __name__ == "__main__":
    # take args from the promp
    arg = sys.argv
    DB_HOST = 'localhost'
    DB_USER = arg[1]
    DB_PASS = arg[2]
    DB_NAME = arg[3]
    ARG_WORD = arg[4]

    data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    # connect to db
    conn = MySQLdb.connect(*data)

    # create cursor
    cursor = conn.cursor()

    # exe query
    query = "SELECT * FROM states WHERE name"
    query_part_two = "LIKE BINARY '{}' ORDER BY states.id ASC".format(ARG_WORD)

    cursor.execute(f'{query} {query_part_two}')

    # Fetch the results of a select
    res = cursor.fetchall()

    # print response
    for i in res:
        print(i)
