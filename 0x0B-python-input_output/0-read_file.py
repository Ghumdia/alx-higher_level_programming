#!/usr/bin/python3
"""Reads a file in stout"""


def read_file(filename=""):
    with open("my_file_0.txt", mode="r", encoding="utf-8") as f:
        for line in f:
            print(line, end="")
