#!/usr/bin/python3

# Lists all states from the database hbtn_0e_0_usa.

import sys
#Imports both sys and MySQLdb module
import MySQLdb
#Imports both sys and MySQLdb module

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
c = db.cursor()
c.execute("SELECT * FROM `states`")
[print(state) for state in c.fetchall()]
