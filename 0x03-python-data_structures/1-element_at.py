#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    elif idx not in my_list:
        return (None)
    else:
        num = my_list[idx]
        return (num)
