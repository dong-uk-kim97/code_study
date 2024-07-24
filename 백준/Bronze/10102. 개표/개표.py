t = int(input())
s = input()
a_cnt = s.count("A")
b_cnt = s.count("B")
if a_cnt > b_cnt:
    print("A")
elif a_cnt < b_cnt:
    print("B")
else:
    print("Tie")