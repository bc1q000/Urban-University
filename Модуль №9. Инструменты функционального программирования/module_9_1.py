def apply_all_func(ins_list, *functions):
    dict_ = {}
    for func in functions:
        dict_[f'{func.__name__}'] = func(ins_list)
    return dict_

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))