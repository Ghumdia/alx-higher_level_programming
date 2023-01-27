#!/usr/bin/python3
import MySQLdb
db = MySQLdb.connect(user="username", password="password", db="name", port=3306)
db.query("""
