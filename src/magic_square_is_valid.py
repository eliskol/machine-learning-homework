def is_valid(square):
    for row in square:
        if sum(row) != 15:
            return False
    for i in range(3):
        if (square[0][i] + square[1][i] + square[2][i]) != 15:
            return False
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if (i in square[0] and i in square[1]) or (i in square[0] and i in square[2]) or (i in square[1] and i in square[2]):
            return False
    if square[0][0] + square[1][1] + square[2][2] != 15 or square[0][2] + square[1][1] + square[2][0] != 15:
        return False
    return True
