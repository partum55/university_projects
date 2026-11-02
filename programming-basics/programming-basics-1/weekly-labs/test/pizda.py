def number_of_transitive_closure(n: int) -> int:
    """
    Given size of set, calculate the number of transitive closures of relations on given set .
    :param n: int, size of set
    :return: int, number of transitive closures of relations on given set

    # >>> number_of_transitive_closure(1)
    2
    # >>> number_of_transitive_closure(2)
    11
    # >>> number_of_transitive_closure(3)
    """
    count = 0
    count_m = 0
    for m in range(2 ** (n * n)):
        string_matrix: list[int] = [int(num) for num in f'{bin(m)[2:]:0>{n*n}}']
        matrix: list[list[int]] = [list(row) for row in zip(*[iter(string_matrix)]*n)]
        if is_matrix_trans(matrix):
            count += 1
        count_m += 1
        # if count_m % 10000 == 0:
        #     print(count_m)
    return count


def is_matrix_trans(matrix: list[list[int]]) -> bool:
    square_matrix = dot(matrix, matrix)
    # temp = deepcopy(matrix)
    # size = len(matrix)
    # for i in range(size):
    #     for j in range(size):
    #         temp[i][j] = any([matrix[i][step] & matrix[step][j] for step in range(size)])

    # for i in range(size):
    #     for j in range(size):
    #         if temp[i][j] != matrix[i][j]:
    #             return False
    return array_equal(square_matrix, matrix)
