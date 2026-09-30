def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []

    fl = len(mat[0])
    for r in mat:
        if len(r) != fl:
            raise ValueError()

    if fl == 0:
        return []

    result = []
    for ci in range(fl):
        nr = []
        for ri in range(len(mat)):
            nr.append(mat[ri][ci])
        result.append(nr)

    return result


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    fl = len(mat[0])
    result = []
    for r in mat:
        if len(r) != fl:
            raise ValueError()

        rs = 0
        for v in r:
            rs += v
        result.append(rs)

    return result


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []

    fl = len(mat[0])
    for r in mat:
        if len(r) != fl:
            raise ValueError()

    if fl == 0:
        return []

    result = []
    for ci in range(fl):
        cs = 0
        for ri in range(len(mat)):
            cs += mat[ri][ci]
        result.append(cs)

    return result



#1 transpose
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

#2 row_sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

#3 col_sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))

