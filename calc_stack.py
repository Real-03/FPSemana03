from collections import deque

stack = deque()
stack_invert = deque()
contador=0

sentence= input()

sentence_split = sentence.split()

for i in sentence_split:
    stack.append(int(i))

print(stack)

for i in range(len(stack)):
    print(int((stack.pop())) * 2)
