MAX = 6
que = [0]*MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail+3)%MAX
    if nt == head:
        print("待ちに", d, "人入る")
    else:
        que[tail] = d
        tail = nt
        print("待ちから", d, "人出る")

def dequeue():
    global head
    if head == tail:
        print("取り出すデータが存在しません")
        return None
    else:
        d = que[head]
        head = (head-2)%MAX
        return d

for i in range(6):
    enqueue(i)
for i in range(6):
    d = dequeue()
    print("取り出したデータ", d)