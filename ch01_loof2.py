#a부터 b까지의 합 구하기

print('정수 a부터 b까지의 합을 구합니다.')
a = int(input('정수 a의 값 입력: '))
b = int(input('정수 b의 값 입력: '))

if a > b:
    a, b = b, a #a와 b를 오름차순으로 정렬 (단일 대입문)

#1.우변의 b,a에 의해 두 값을 압축한 튜플 (b, a) 생성
#2. 대입할 때 튜플 (b, a)를 다시 풀어 b, a로 만든 후 각각 a와 b에 대입.
#뭔소리야? 튜플은 값을 변경못하는 리스트와 비슷하긴 함 근데 이게 뭔데

sum = 0
for i in range(a, b+1):
    sum += i

print(f'정수 a부터 b의 합은 {sum}입니다.')