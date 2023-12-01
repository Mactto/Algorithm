import sys
input = sys.stdin.readline


N = int(input())
stack = []
for _ in range(N):
    command = input().rstrip()
    
    #push
    if len(command) > 2:
        stack.append(int(command[2:]))
    
    #pop
    elif command == '2':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    
    #size
    elif command == '3':
        print(len(stack))

    #empty
    elif command == '4':
        print(1 if len(stack)==0 else 0)
    
    #top
    elif command == '5':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])