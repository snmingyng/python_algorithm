#반복하는 알고리즘

print('1부터 n까지 정수으 합을 구합니다.')
n = int(input('n을 입력하세요.: '))

sum = 0
# i = 1
# while i <= n:   #i가 n보다 작거나 같을때만 반복
#     sum += i    #sum에 i를 더한 값을 대입한다.
#     i += 1      #i에 1을 더해 대입한다.

#while문은 마지막 i가 n+1이 된다. (n보다 크면 중지되므로)

for i in range(1, n+1): 
    #range()함수는 이터러블 객체(반복할 수 있는 객체)를 생성한다.
    #range(a, b): a이상 b미만인 수를 차례로 나열하는 수열. ->그래서 마지막 i가 n이 된다.
    sum +=i

#for문은 마지막 i가 n과 같다

print(f'1부터 n까지 정수의 합은 {sum} 입니다.')
print(f'i값은 {i}')