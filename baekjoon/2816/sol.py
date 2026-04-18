import sys
input = sys.stdin.readline

N = int(input())
channels = [input().strip() for _ in range(N)]

result = ""

# 1. KBS1을 맨 위로 올리기
idx1 = channels.index("KBS1")

# 커서를 KBS1 위치까지 내림 (1번 버튼)
result += "1" * idx1

# KBS1을 위로 올림 (4번 버튼)
result += "4" * idx1

# 리스트도 실제로 바꿔줌
channels.pop(idx1)
channels.insert(0, "KBS1")


# 2. KBS2를 두 번째로 올리기
idx2 = channels.index("KBS2")

# 커서를 KBS2 위치까지 내림 (1번 버튼)
result += "1" * idx2

# KBS2를 위로 올림 (4번 버튼)
result += "4" * (idx2 - 1)

print(result)