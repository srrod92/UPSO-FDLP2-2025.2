from collections import deque

## Las son estructura del tipo FIFO - First in First OUT 

## Cuando agrego, lo hago en la ultima pos, y cuando saco, lo hago desde la primera.


queue = deque()

queue.append(5)
queue.append(1)
queue.append(3)
queue.append(7)
queue.append(2)
queue.append(5)
queue.append(9)

print(queue)

print(queue.popleft())

print(queue)
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())





