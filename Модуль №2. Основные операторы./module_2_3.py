list_ = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# list_1 = [42, 69, 322, 13, 1, 99, 5, 9, 8, 7, 6, 100]
count = 0
a = list_[count]
list_length = len(list_)

while list_[count] >= 0 or list_[count] == list_length - 1:
    if list_[count] == 0:
        count += 1
        continue
    else:
        print(list_[count])
        count += 1
