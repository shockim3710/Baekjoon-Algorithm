import sys

editor = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline())

editorAdd = []

for i in range(M):
    com = sys.stdin.readline().strip()

    if com[0] == 'L' and editor != []:
        editorAdd.append(editor.pop())
    elif com[0] == 'D' and editorAdd != []:
        editor.append(editorAdd.pop())
    elif com[0] == 'B' and editor != []:
        editor.pop()
    elif com[0] == 'P':
        editor.append(com[2])

print(''.join(editor + list(reversed(editorAdd))))