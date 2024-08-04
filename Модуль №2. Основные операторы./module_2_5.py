def get_matrix(n = int(input()), m =  int(input()), value = int(input())):
    matrix = []
    for i in range(n):
        list = []
        matrix.append(list)
        for j in range(m):
            list.append(value)


    print(matrix)

get_matrix()
