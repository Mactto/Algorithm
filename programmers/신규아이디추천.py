import re


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    new_id = re.sub(r"[^a-z0-9-_.]", "", new_id)
    new_id = re.sub(r"[.]+", ".", new_id)
    new_id = re.sub(r"^[.]", "", new_id)
    new_id = re.sub(r"[.]$", "", new_id)
    if new_id == '':
        new_id = 'a'
    if len(new_id) > 15:
        new_id = new_id[:15]
        new_id = re.sub(r"[.]$", "", new_id)
    if len(new_id) < 3:
        new_id += new_id[len(new_id)-1] * (3 - len(new_id))
    print(new_id)

    return answer


if __name__ == "__main__":
    new_id = input()
    print(solution(new_id))
