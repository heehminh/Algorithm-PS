# 백준 15721 번데기
# A: 게임을 진행하는 사람
# T: 구하고자 하는 번째 (T번째로 부른)
# N: 0->뻔 1->데기 

# (1) 뻔 - 데기 - 뻔 - 데기 - 뻔 - 뻔 - 데기 - 데기 : 8번 
# 뻔:3+1, 데기:3+1
# 몇번째인지, 1 1 2 2 / 3 4 3 4 

# (2) 뻔 - 데기 - 뻔 - 데기 - 뻔 - 뻔 - 뻔 - 데기 - 데기 - 데기 : 10번 
# 뻔:3+2, 데기:3+2: 누적-> 3(1+2)번
# 몇번째인지, (4+를 할것) 1 1 2 2 3 4 5 3 4 5=> 5 5 6 6 / 7 8 9 7 / 8 9 

# (N) : 6+2N번 게임이 진행됨 
# 뻔:3+N, 데기:3+N: 누적 -> 3(1+2+...+N)

# 8 2 0 -> 2 < 4: 1회차에서 찾아야 함 
# 4 6 1 -> 4 < 6 < 9: 2회차에서 찾아야 함 

# 이전 회차에 뻔 데기를 누적 몇 번 외쳤는지 저장

A = int(input())
T = int(input())
N = int(input())

games = [] # 게임 진행 상황 (튜플로 저장)
bbun = 1 # 뻔 을 외친 횟수
degi = 1 # 데기 를 외친 횟수
cnt = 0 # 몇번째 게임인지 

while(True):
    num = bbun # 이전 회차에서 뻔 or 데기를 외친 누적 횟수
    cnt += 1
    
    # 1) 처음에 뻔 - 데기 - 뻔 - 데기 이 4번 반복은 동일함
    for _ in range(2):
        games.append((bbun, 0))
        bbun += 1
        games.append((degi, 1))
        degi +=1 

    # 2) 뻔 - 뻔 - 반복부분
    # (1): 2번, (2): 3번, (cnt): cnt+1번
    for _ in range(cnt+1):
        games.append((bbun, 0))
        bbun +=1 
    
    for _ in range(cnt+1):
        games.append((degi, 1))
        degi += 1
        
    # 3) 정답 찾기
    # 4 <= 6 < 9: 2회차에서 찾아야 함 
    if (num <= T < bbun):
        print(games.index((T, N)) % A)
        break