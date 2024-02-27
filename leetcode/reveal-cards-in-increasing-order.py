class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        queue = deque()
        for i in range(len(deck)):
            queue.append(deck[i])

        ans = [0] * len(deck)
        indexes = deque()
        for i in range(len(deck)):
            indexes.append(i)
        
        while indexes:
            ind = indexes.popleft()
            ans[ind] = queue.popleft()
            if indexes:
                indexes.append(indexes.popleft())

        return ans







        # deck.sort()
        # first = deque()
        # second = []
        # if len(deck)%2 == 0:
        #     i = 0
        #     n = len(deck)//2
        #     while i < n:
        #         first.append(deck[i])
        #         second.append(deck[i+n])
        #         i+=1
        # else:
        #     i = 0
        #     n = len(deck)//2+1
        #     while i < n:
        #         if i == n-1:
        #             first.append(deck[i])
        #         else:
        #             first.append(deck[i])
        #             second.append(deck[i+n])
        #         i+=1
        # print(first)
        # print(second)
        # second_stack = deque()           
        # for i in range(len(second)):
        #     if i == 0 and i % 3 == 0 or i % 3 == 2:
        #         second_stack.append(second[i])
        #     elif i % 3 == 1:
        #         if second[i] > second_stack[-1]:
        #             temp = second_stack.pop()
        #             second_stack.append(second[i])
        #             second_stack.append(temp)
        # ans = []
        # while first and second_stack:
        #     ans.append(first.popleft())
        #     ans.append(second_stack.popleft())
        # while first:
        #     ans.append(first.popleft())
        # while second_stack:
        #     ans.append(second_stack.popleft())
        # return ans

  
        





        