# 7181. 최대공약수

N, M = map(int, input().split())

for i in range(min(N, M), 0, -1) :
    if N%i == 0 and M%i == 0:
        gcd = i
        break

print(i)

'''
문제:
최대공약수란 어떤 두 개 이상의 자연수들이 있을 때, 두 수의 공통된 약수 중 가장 큰 수를 말합니다.
서로 다른 두 자연수 N, M이 주어졌을 때, 두 수의 최대공약수를 출력하는 프로그램을 만드세요.

테스트케이스:
124 512     >   4
14 18       >   2

입력값 설명:
첫째 줄에 서로 다른 두 자연수 N ,M이 공백을 두고 주어집니다. (1 ≤ N ≤ 100,000) (1 ≤ M ≤ 100,000)

출력값 설명:
두 자연수 N, M의 최대공약수를 출력합니다.

'''