import sys

memo = set()

for x in range(10):
  a = int(input()) % 42
  memo.add(a)

print(len(memo))