def rm_dups(x):
    return list(dict.fromkeys(x))
my_list = rm_dups(['a', 'b', 'a', 'c', 'b'])
print(my_list)
