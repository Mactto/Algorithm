while True:
    x, y, z = map(int, input().split())
    
    if x == 0 and y == 0 and z == 0:
        break

    if sum([x, y, z]) - (2 * max([x, y, z])) < 1:
        print("Invalid")
    elif x == y == z:
        print("Equilateral")
    elif x == y or y == z or z == x:
        print("Isosceles")
    else:
        print("Scalene")