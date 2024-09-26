stack = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        stack.append(a)
if not stack:
    print(-1)
else:
    print(sum(stack))
    print(min(stack))