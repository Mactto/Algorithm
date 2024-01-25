def solution(wallpaper):
    lux, luy, rdx, rdy = 51, 51, 0, 0

    wallpaper = [list(wall) for wall in wallpaper]

    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i+1 > rdx:
                    rdx = i + 1
                if j+1 > rdy:
                    rdy = j + 1

    return [lux, luy, rdx, rdy]