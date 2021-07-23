import sys

n = int(input())
result = set()

for i in range(n):
    name, log = map(str, sys.stdin.readline().split())

    if log == 'enter':
        result.add(name)
    elif log == 'leave':
        result.remove(name)

result = list(result)
result.sort(reverse=True)

print("\n".join(result))