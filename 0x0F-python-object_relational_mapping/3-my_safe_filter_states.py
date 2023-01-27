#!/usr/bin/python3

"""
Takes an argument and searchs the entire
database for that argument taken in
"""

import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM `states` \
            WHERE name LIKE BINARY %s ORDER \
            BY id ASC"
    st = sys.argv[4]
    cur.execute(query, (st,))
    for state in cur.fetchall():
        print(state)

    cur.close()
    db.close()
