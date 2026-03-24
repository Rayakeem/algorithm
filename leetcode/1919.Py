import sys

#dic으로 저장하기. 키:요소, 값:빈도 수
def cnt(s) :
  d = {}
  for c in s:
    d[c] = d.get(c , 0) + 1
  return d

a = cnt(input().strip())
b = cnt(input().strip())

ans = 0

#비교
for ch in set(a.keys()) | set(b.keys()):
  ans += abs(a.get(ch, 0) - b.get(ch, 0))

print(ans)