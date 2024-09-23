while True:
    sentence = input()
    cnt = 0
    if sentence == "#":
        break
    else:
        for i in sentence:
            if i in ["a","e","i","o","u","A","E","I","O","U"]:
                cnt +=1
        print(cnt)