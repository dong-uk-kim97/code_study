number = {"-":0,"\\":1,"(":2,"@":3,"?":4, ">":5,"&":6,"%":7,"/":-1}
while True:
    sentence = input()
    if sentence == "#":
        break
    else:
        summ = 0
        for i in range(len(sentence)):
            summ += number[sentence[i]] * 8 ** (len(sentence)-i-1)
        print(summ)