def check_vowel(word: str):
    vowel = ['a', 'e', 'i', 'o', 'u']

    for v in vowel:
        if v in word:
            return True

    return False

def check_continuous_third(word: str):
    vowel = ['a', 'e', 'i', 'o', 'u']
    word_len = len(word)

    if word_len < 3:
        return True
    
    for i in range(word_len - 2):
        if word[i] in vowel and word[i+1] in vowel and word[i+2] in vowel:
            return False
        elif word[i] not in vowel and word[i+1] not in vowel and word[i+2] not in vowel:
            return False
    return True


def check_continuous_twice(word: str):
    if len(word) < 2:
        return True
    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            if word[i] == 'e' or word[i] == 'o':
                continue
            return False
    return True

def check(password: str):
    return check_vowel(password) and check_continuous_twice(password) and check_continuous_third(password)

while True:
    password = input()

    if password == 'end':
        break

    if check(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")
