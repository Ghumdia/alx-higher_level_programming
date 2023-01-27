#!/usr/bin/python3
#Filters out the states beginning with the alphabet N(uppercase)

import sys
import MySQLdb

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM `states` WHERE name LIKE 'N%'")
for state in c.fetchall():
    print(state)
