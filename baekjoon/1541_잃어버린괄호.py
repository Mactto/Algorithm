def check(f):
    if '+' in f: return True
    else: return False

def algorithm():
    global sp
    if sp[0] == '':
        sp.pop(0)
        result = 0
    else:
        if check(sp[0]):
            result = eval(sp.pop(0))
        else:
            result = int(sp.pop(0))
    
    for s in sp:
        if check(s):
            result -= eval(s)
        else:
            result -= int(s)
    return result
        
if __name__ == "__main__":
    fomula = input()
    sp = fomula.split('-')
    print(algorithm())