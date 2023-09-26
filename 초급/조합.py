# 7193. 조합
from math import factorial
combi = 0

A, B = map(int, input().split())
combi = factorial(A) // (factorial(A-B)*factorial(B))

print(combi)

'''
문제:
정수 A와 B가 입력될 때 A개의 원소에서 B개의 원소를 뽑는 조합에 대한 총 경우의 수를 출력하는 프로그램을 작성하세요.

테스트케이스:
105     >   252
72      >   21

입력값 설명:
첫 번째 줄에 정수 A와 B가 공백을 기준으로 입력됩니다. (1 ≤ B ≤ A ≤ 30)

출력값 설명:
A개의 원소에서 B개의 원소를 뽑는 조합에 대한 총 경우의 수를 출력합니다.

'''