def calc_cartesian_product(sets):
    points = [[]]
    for _set in sets:
        extended_points = []
        for point in points:
            for elem in _set:
                extended_points.append(point + [elem])
        points = list(extended_points)
    return points


print(calc_cartesian_product([['a', 'b', 'c'], [1, 2, 3], ['Y', 'Z']]))
