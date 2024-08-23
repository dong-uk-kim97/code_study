a,b = list(map(int,input().split(' ')))
c,d = list(map(int,input().split(' ')))

numerator = (b*c+a*d) #분자
denominator = b*d #분모

#최대공약수
def GCD(x,y):
    while y:
        x,y = y,x%y
    return x

gcd = GCD(numerator,denominator)

numerator = int(numerator/gcd) #최대공약수로 나누기(약분)
denominator = int(denominator/gcd) #최대공약수로 나누기(약분)

print(f"{numerator} {denominator}") #정답