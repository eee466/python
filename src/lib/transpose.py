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