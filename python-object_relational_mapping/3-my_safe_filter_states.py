#!/usr/bin/python3
""" SQL Injection """

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
    query = "SELECT * FROM states WHERE name LIKE %(s)s ORDER BY states.id ASC"
    
    
    cursor.execute(query, {'s': ARG_WORD})

    # Fetch the results of a select
    res = cursor.fetchall()

    # print response
    for i in res:
        print(i)
