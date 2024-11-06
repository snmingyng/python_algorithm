#중앙값 구하기

def med3(a, b, c):
    if a >= b:      #a가 b보다 크거나 같을 때(c의 위치를 가늠해야 한다.)
        if b >= c:      #a>=b면서 b>=c면 b가 중앙값이다. (a>=b>=c)
            return b
        elif c >= a:    #a>=b면서 c>=a면 a가 중앙값이다. (c>=a>=b)
            return a
        else:
            return c    #a>=b면서 a>=c고 c>=b면 c가 중앙값이다. (a>=c>=b) 
    elif a > c:     #a<b면서 c<a면 a가 중앙값이다. (b>a>c)
        return a    
    elif b > c:     #a<b면서 a<=c면서 b>c일 때 c가 중앙값이다.(b>c>a)
        return c
    else:           #a<b면서 a<=c면서 b<c일 때 b가 중앙값이다. (a<b<c)
        return b


"""def med3(a, b, c):  #같은 기능을 하는 코드
    if (b >= a and c <= a) or (b <= a and c >= a):
        #a와 b의 비교를 마친 상태
        return a
    elif (a > b and c < b) or (a < b and c > b):
        #elif문에서 또 a와 b를 비교하는건 효율적이지 않다
        return b
    return c"""

print('세 정수의 중앙값을 구합니다')
a = int(input('정수 a의 값을 입력: '))
b = int(input('정수 b의 값을 입력: '))
c = int(input('정수 c의 값을 입력: '))

print(f'중앙값은 {med3(a, b, c)}입니다.')