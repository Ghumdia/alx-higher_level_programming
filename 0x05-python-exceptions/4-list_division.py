#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
            newlist.append(div)
        except TypeError:
            print("wrong type")
            div = 0
            newlist.append(div)
        except ZeroDivisionError:
            print("division by 0")
            div = 0
            newlist.append(div)
        except IndexError:
            print("out of range")
            div = 0
            newlist.append(div)
    return newlist
