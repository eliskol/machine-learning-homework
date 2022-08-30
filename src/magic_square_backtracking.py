from magic_square_is_valid import is_valid


def is_hopeless(square):
    for i in range(3):
        if square[0][i] is not None and square[1][i] is not None and square[2][i] is not None:
            if square[0][i] + square[1][i] + square[2][i] != 15:
                return True
        if square[i][0] is not None and square[i][1] is not None and square[i][2] is not None:
            if square[i][0] + square[i][1] + square[i][2] != 15:
                return True
    for i in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        if (i in square[0] and i in square[1]) or (i in square[0] and i in square[2]) or (i in square[1] and i in square[2]):
            return True
    try:
        if square[0][0] + square[1][1] + square[2][2] != 15 or square[0][2] + square[1][1] + square[2][0] != 15:
            return True
    except TypeError:
        return False
    return False

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

square = [[None for i in range(3)] for i in range(3)]

for num1 in digits:
    digits2 = list(digits)
    digits2.remove(num1)
    for num2 in digits2:
        digits3 = list(digits2)
        digits3.remove(num2)
        for num3 in digits3:
            digits4 = list(digits3)
            digits4.remove(num3)
            square = [[num1, num2, num3], [None, None, None], [None, None, None]]
            if is_hopeless(square):
                continue
            for num4 in digits4:
                digits5 = list(digits4)
                digits5.remove(num4)
                square = [[num1, num2, num3], [num4, None, None], [None, None, None]]
                if is_hopeless(square):
                    continue
                for num5 in digits5:
                    digits6 = list(digits5)
                    digits6.remove(num5)
                    square = [[num1, num2, num3], [num4, num5, None], [None, None, None]]
                    if is_hopeless(square):
                        continue
                    for num6 in digits6:
                        digits7 = list(digits6)
                        digits7.remove(num6)
                        square = [[num1, num2, num3], [num4, num5, num6], [None, None, None]]
                        if is_hopeless(square):
                            continue
                        for num7 in digits7:
                            digits8 = list(digits7)
                            digits8.remove(num7)
                            square = [[num1, num2, num3], [num4, num5, num6], [num7, None, None]]
                            if is_hopeless(square):
                                continue
                            for num8 in digits8:
                                digits9 = list(digits8)
                                digits9.remove(num8)
                                square = [[num1, num2, num3], [num4, num5, num6], [num7, num8, None]]
                                if is_hopeless(square):
                                    continue
                                for num9 in digits9:
                                    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    square = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]
                                    if is_valid(square):
                                        print(square)
