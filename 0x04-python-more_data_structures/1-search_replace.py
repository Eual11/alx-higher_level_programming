#!/usr/bin/python3
def search_replace(my_list, search, replace):
    outlist = my_list[:]
    while outlist.count(search) >= 1:
        place = outlist.index(search)
        outlist[place] = replace

    return outlist
