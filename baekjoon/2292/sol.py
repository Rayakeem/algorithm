import sys
input = sys.stdin.readline

N = int(input())

layer = 1        # 현재 층 (답)
max_num = 1      # 현재 층까지의 최대 번호

while N > max_num:
    max_num += 6 * (layer)
    layer += 1

print(layer)