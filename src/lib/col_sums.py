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
