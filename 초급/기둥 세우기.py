# 7197. 기둥 세우기

N, M = map(int, input().split())
pillar = []
count = 0

# 입력받기 (1은 빈칸 , 0은 기둥있는 칸)
for i in range(N) :
    pillar.append(list(map(int, input().split())))

# 기둥이 존재하는지 확인
for i in range(N) :
    if 0 not in pillar[i] :
        count += 1
    
print(count)

'''
문제:
오래된 궁전이 세월의 무게를 이기지 못하고 무너지려고 합니다. 관리당국에서는 궁전 곳곳에 기둥을 세우는 보수 공사를 하려고 합니다. 
직사각형 형태의 궁전을 형성하는 모든 가로, 세로 줄에 대해서 적어도 기둥이 하나씩은 존재하도록 만들고자 할 때 세워야 하는 기둥의 최솟값을 출력하세요.

테스트케이스:
3 3
1 1 1
1 1 1
1 1 1       >   3

4 3
0 1 1
1 0 0
0 1 0
1 0 1       >   0

입력값 설명:
첫째 줄에 궁전의 세로 크기 N과 가로 크기 M이 주어집니다. N과 M은 50보다 작거나 같은 자연수입니다.
둘째 줄부터 N개의 줄에는 궁전의 상태가 주어집니다. 궁전의 상태는 1은 빈칸, 0은 기둥이 있는 칸입니다.

출력값 설명:
세워야 하는 기둥의 최솟값을 출력합니다.

'''