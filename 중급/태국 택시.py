# 7213. 태국 택시
# 알고리즘 : 최소 스패닝 트리(MST, Minimum Spanning Tree)

# 특정 원소의 부모를 찾는 함수.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소를 합치는 함수. 두 원소를 연결할 때, 더 작은 원소를 부모로 설정.
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a <b:
        parent[b] = a
    else :
        parent[a] = b

N, M = map(int, input().split())
edge = [ list(map(int, input().split())) for _ in range(M)]

edge.sort(key = lambda x : x[2])        # 비용 순 정렬
parent = list(range(N+1))

# 최소 신장 트리 생성
min_cost = 0

for e in edge:
    a, b, cost = e
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        min_cost += cost
        
print(min_cost)

'''
문제:
태국의 한 도시로 출장을 온 민혁은 택시를 타고 모든 마을을 방문하려 합니다. 
이 도시의 택시 체계는 특이합니다. 
각 택시는 어떤 두 마을 사이만 운행하므로, 어떤 택시를 타고 하나의 마을에서 출발해 다른 마을에 도착했다면 다른 택시로 갈아타야 합니다. 
타고 싶은 택시들은 모두 전날에 선불로 요금을 내고 예약해야 합니다. 
예약한 택시는 몇 번을 타더라도 추가비용 없이 자유롭게 이용할 수 있습니다.

도시에 N개의 마을과 M대의 택시가 있을 때, 택시만으로 모든 마을을 방문하려면 택시 예약에 적어도 얼마가 드는지 출력하는 프로그램을 작성하세요. 

테스트케이스:
3 2
1 2 7
1 3 5       >  12

4 5
1 3 10
2 3 20
4 1 30
3 4 40
2 4 50      >   60

입력값 설명:
첫째 줄에 마을의 수 N(2 ≤ N ≤ 100)과 택시의 수 M(1 ≤ M ≤ 1,000)이 주어집니다.
이후 M개의 줄에 걸쳐 각 줄에 a, b, c가 공백을 구분으로 입력됩니다. 
도시 a와 도시 b를 양방향으로 연결하는 예약비용이 c인 택시를 의미합니다. (a ≠ b, 1 ≤ a, b ≤ N, 1 ≤ c ≤ 100)
입력에서 주어진 도시를 정점으로, 택시 노선을 간선으로 가정하면 연결 그래프임을 보장합니다.

출력값 설명:
택시만으로 모든 마을을 방문하려면 택시 예약에 적어도 얼마가 드는지 출력합니다.
'''