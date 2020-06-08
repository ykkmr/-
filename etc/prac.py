#직각삼각형의 밑변이 x, 높이가 y일 때 남은 변(대각선)의 길이를 구하는 함수를 만들어주세요.

def tri(x,y):
    a = x**2
    b = y**2
    c = a + b
    print(c**(1/2))

tri(6,8)

def pita(): 
    a = input('첫 숫자를 입력하세요')
    x = float(a)
    b = input('두번째 숫자를 입력하세요')
    y = float(b)
    result = (x**2 + y**2)**0.5
    print(result)
pita()

