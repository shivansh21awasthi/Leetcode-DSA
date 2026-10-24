class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends1=set(deadends)
        if '0000' in deadends1:
            return -1
        queue=deque([('0000',0)])
        visit={'0000'}
        while queue:
            curr,move=queue.popleft()
            if curr==target:
                return move
            for wheel in range(4):
                digit=int(curr[wheel])
                for rot in(-1,1):
                    newdigit=(digit+rot)%10
                    newstate=curr[:wheel]+str(newdigit)+curr[wheel+1:]
                    if newstate not in deadends1 and newstate not in visit:
                        queue.append((newstate,move+1))
                        visit.add(newstate)
        return -1        

        