#!/usr/bin/python3
""" Task 5 """

import sys
import MySQLdb
if __name__ == "__main__":
    # take args from the promp
    arg = sys.argv
    DB_HOST = 'localhost'
    DB_USER = arg[1]
    DB_PASS = arg[2]
    DB_NAME = arg[3]
    STATE = arg[4]

    data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]

    # connect to db
    conn = MySQLdb.connect(*data)

    # create cursor
    cursor = conn.cursor()

    # exe query
    query = "SELECT c.name, s.name FROM cities AS c"
    query_two = "JOIN states AS s ON c.state_id = s.id ORDER BY c.id ASC"

    cursor.execute(f'{query} {query_two}')

    # Fetch the results of a select
    res = cursor.fetchall()
    temp = ''

    # print response
    for i in res:
        if i[1] == STATE:
            if temp != '':
                temp += ', '
            temp += (i[0])
    print(temp)
