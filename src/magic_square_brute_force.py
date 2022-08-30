from magic_square_is_valid import is_valid

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
            for num4 in digits4:
                digits5 = list(digits4)
                digits5.remove(num4)
                for num5 in digits5:
                    digits6 = list(digits5)
                    digits6.remove(num5)
                    for num6 in digits6:
                        digits7 = list(digits6)
                        digits7.remove(num6)
                        for num7 in digits7:
                            digits8 = list(digits7)
                            digits8.remove(num7)
                            for num8 in digits8:
                                digits9 = list(digits8)
                                digits9.remove(num8)
                                for num9 in digits9:
                                    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                                    square = [[num1, num2, num3], [num4, num5, num6], [num7, num8, num9]]
                                    if is_valid(square):
                                        print(square)
