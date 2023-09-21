# 7188. 누적 합

N = int(input())
tree_list = []

if N == 1:
    print(int(input()))
else :
    num_list = list(map(int, input().split()))
    
    # 트리 높이 계산
    height = (len(num_list).bit_length())
    # print(height)   # len(num_list) = 6일 때 3

    # 누적합 트리 생성    
    for i in range(height+1) :
        tree_list.append([0]*(2**i))
    # print(tree_list)

    # 제일 아래층에 값 채우기
    for i in range(N):
        tree_list[height][i] = num_list[i]
    # print(tree_list)

    # 누적합 계산
    for i in range(height, -1, -1):
        for j in range(0, len(tree_list[i])//2):
            tree_list[i-1][j] = tree_list[i][2*j] + tree_list[i][2*j+1]
    # print(tree_list)

    # 출력
    for i in tree_list:
        print(*i)
    
''' 추가사항
- bit_length()
    : 비트의 개수 확인
    10진수 6의 경우 8비트 필요. 2^3 -> 3 리턴

'''

'''
문제:
누적 합 트리란 각 원소가 2개씩 누적되어 합해지는 형태를 가진 트리를 의미합니다. 
승훈은 이진 트리 자료구조를 공부하다가 누적 합을 가지는 이진 트리를 만들어보고 싶다는 생각을 했습니다. 
하지만 자료구조를 3번이나 재수강 했지만 모두 C+을 받은 승훈은 스스로 이러한 프로그램을 작성할 능력이 없습니다.
그러므로 우리가 승훈을 대신하여 주어진 원소로 누적 합 이진 트리를 만드는 프로그램을 작성해봅시다.

테스트케이스:
6
1 9 3 8 4 5     >   30
                    21 9
                    10 11 9 0
                    1 9 3 8 4 5 0 0
                    
9
4 5 3 8 4 2 1 1 1       >   29
                            28 1
                            20 8 1 0
                            9 11 6 2 1 0 0 0
                            4 5 3 8 4 2 1 1 1 0 0 0 0 0 0 0

입력값 설명:
첫 번째 줄에는 원소의 갯수 N(1 ≤ N ≤ 4,095)이 주어집니다.
두 번째 줄에는 각 원소의 값 K(1 ≤ K ≤ 1,000)이 공백을 구분으로 주어집니다.

출력값 설명:
누적 합을 가지는 이진 트리의 모든 원소를 최상단 원소부터 2의 거듭제곱 개수로 차례대로 출력합니다.
이 때 출력되는 이진 트리는 완전이진트리 형태입니다. 특정 위치의 원소가 없는 경우 그 값은 0이라고 간주합니다.

'''