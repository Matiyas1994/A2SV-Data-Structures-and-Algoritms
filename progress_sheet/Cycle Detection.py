def has_cycle(head):
    if head == None:
        return
    ans = 0
    curr = head
    myhash = set()
    while (curr != None):
        if curr in myhash:
            return 1
        else:
            myhash.add(curr)
            curr= curr.next
    return ans
