#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 and idx > (len(my_list) - 1):
        return (my_list)
    else:
        tmp = [x for x in my_list]
        tmp[idx] = element
        return (tmp)
