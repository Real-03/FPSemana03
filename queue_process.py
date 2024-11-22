from collections import deque

queue = deque()


sentence= input()

sentence_split = sentence.split()

for i in sentence_split:
    queue.appendleft(i)

print(queue)
for i in range(len(queue)):
    word= queue.pop()
    if(word.find("a")!= -1):
        print(word)
