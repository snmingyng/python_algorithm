#a부터 b까지 정수의 합 구하기

print('정수 a부터 b까지의 합을 구합니다.')
a = int(input('정수 a의 값 입력: '))
b = int(input('정수 b의 값 입력: '))

if a > b:
    a, b = b, a

sum = 0
for i in range(a, b+1):
    if i < b:   #i가 b보다 작으면 합을 구하는 과정 i + 출력
        print(f'{i} + ', end='')
    else:       #i가 b보다 크거나 같으면 최종 i값과 함께 i = 출력
        print(f'{i} = ', end='')
    sum += i   #sum에 i를 더하는 과정


print (sum)