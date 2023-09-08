# 7223. 떡 하나 주면 안 잡아먹지
# 알고리즘 : BFS, Deque

from collections import deque

N = int(input())        # N*N 격자
tiger = [list(map(int, input().split())) for _ in range(N)]     # 호랑이가 요구하는 떡의 개수
result = [[float('inf')] * N for _ in range(N)]     # 결과값을 담을 격자

result[0][0] = tiger[0][0]      # 초기값 지정

# 상하좌우 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

route = deque()
route.append([0, 0])    # 이동 좌표 저장

# 종료지점으로 도착할 때까지 반복
while route :
    x, y = route.popleft()

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]   # 현좌표에서 상하좌우 좌표 확인
        
        if 0<=nx<N and 0<=ny<N :    # 최소 떡 개수 확인
            cost = result[x][y] + tiger[nx][ny]
            if result[nx][ny] > cost :
                result[nx][ny] = cost
                route.append([nx, ny])

print(result[N-1][N-1])

'''
문제 :
떡장사를 마치고 집에 가는 아낙네에게는 집에서 엄마를 애타게 기다리는 사랑스러운 오누이가 있습니다.
집에 가는 길은 N행 N열, 총 N * N 칸의 격자로 나뉘며, 모든 칸에는 호랑이가 한 마리씩 살고 있습니다.
이 호랑이들은 떡을 매우 좋아하여 "떡 몇 개 주면 안 잡아먹지!"라며 위협을 합니다.

제일 왼쪽 위 1행 1열의 칸에 서 있는 아낙네는 제일 오른쪽 아래 N행 N열의 칸에 있는 집으로 돌아가야 합니다.
아낙네는 상하좌우 중 한 방향으로 인접한 칸으로만 이동할 수 있으며, 길 밖으로 나가는 것은 불가능합니다. 
집에 가는 길에 만나는 모든 호랑이에게 반드시 원하는 만큼의 떡을 줘야 하며, 이는 1행 1열의 호랑이와 N행 N열의 호랑이를 포함합니다. 
아낙네가 집으로 돌아가려면 최소 몇 개의 떡이 필요한지 출력하는 프로그램을 작성하세요.

테스트케이스 :
3
1 4 6
2 7 4
4 5 2       ->  14

5
3 62 5 1 8
5 73 9 38 9
1 80 2 92 7
2 59 4 67 4
6 7 3 87 4          ->  80

입력값 설명 :
첫째 줄에 정수 N이 주어집니다. (2 ≤ N ≤ 50)
둘째 줄부터 N개의 줄에 걸쳐 각 칸의 호랑이가 요구하는 떡의 개수가 주어집니다.
둘째 줄의 첫 번째 수가 1행 1열이고, N+1째 줄의 N번째 수가 N행 N열입니다.

출력값 설명 :
아낙네가 집으로 돌아가려면 최소 몇 개의 떡이 필요한지 출력합니다.
'''