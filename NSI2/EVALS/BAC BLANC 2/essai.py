def mg(lst):
    enda = (len(lst) + 1) // 2
    return lst[:enda]


print(mg([]))
print(mg([4, 8, 3]))
print(mg([4, 8, 3, 7]))
