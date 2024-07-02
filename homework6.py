# homework6

# словари
my_dict = {'MTLR': 1500, 'MGNT': 6500, 'LNZL': 13900}
print(my_dict, my_dict['MTLR'], my_dict.get('TRNFP'), sep='\n')
my_dict.update({'GMKN': 132, 'TATN': 710})
print(my_dict)
a = my_dict.pop('MTLR')
print(a)
print(my_dict)

# множества
my_set = {1, 1, 'Python', 'Python', 5, 8.8}
print(my_set)
my_set.update({'Урбан', 'Университет'})
print(my_set)
my_set.discard('Python')
print(my_set)