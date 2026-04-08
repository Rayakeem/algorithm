import sys
input = sys.stdin.readline

N = int(input())

lst = list(map(int, input().split()))

# lst 수열과 같은 수열을 만들어
lenlst = [1] * len(lst)

#i번째랑 이 전 값을 비교해서 크면 lenlst에 길이로 큰 값을 저장, 작으면 ㅃㅇ
#max()로 비교해서 넣는 이유는 현재 자신의 길이값 vs 나보다 작은 요소의 길이 뒤에 붙으면 큰 값 중 큰 것에 붙는 것

for i in range(len(lst)):
  j = 0
  for j in range(i):
    
    if lst[j] < lst[i] :
      lenlst[i] = max( lenlst[i], lenlst[j]+1 )

print(max(lenlst))