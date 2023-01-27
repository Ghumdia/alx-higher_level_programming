#!/usr/bin/python3

"""
    Lists all the states beginning with N int the 
    database hbtn_0e_0_usa
"""

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY `id`")
for state in c.fetchall():
    print(state)
