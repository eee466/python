def flatten(mat: list[list | tuple]) -> list:
    if not isinstance(mat, (list, tuple)):
        raise TypeError()
    
    r = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError()
        for i in row:
            r.append(i)
            
    return r