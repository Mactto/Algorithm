import re


def solution(files):
    temp = []
    for f in files:
        temp.append(re.split(r"([0-9]+)", f))
    answer = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))
    return [''.join(i) for i in answer]


if __name__ == "__main__":
    files = ["img12.png", "img10.png", "img02.png",
             "img1.png", "IMG01.GIF", "img2.JPG"]
    print(solution(files))
