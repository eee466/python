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