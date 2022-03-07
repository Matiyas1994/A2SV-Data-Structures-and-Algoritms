import heapq as h


count = int(input().strip())
Myset = set()
heap = []
for _ in range(count):
    input_ = input().rstrip().split()
    key = int(input_[0])
    if key != 3:
        value = int(input_[1])
    
    if key == 1:
        h.heappush(heap,value)
        Myset.add(value)
    elif key == 2:
        Myset.discard(value)
    elif key == 3:
        while heap[0] not in Myset:
            h.heappop(heap)
        print(heap[0])
