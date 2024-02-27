class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        br, bd, tbd, tbr, cr, cd = 0, 0, 0, 0, 0 ,0
        for val in senate:
            if val == "R": 
                cr+= 1
            else:
                cd+= 1
        queue = deque(senate)
        while queue:
            val = queue.popleft()
            if val == "R":
                if br > 0:
                    br -= 1
                else:
                    tbd+= 1
                    bd+= 1
                    queue.append(val)
            else: 
                if bd > 0:
                    bd -= 1
                else:
                    tbr+= 1
                    br+= 1
                    queue.append(val)

            if tbd >= cd:
                return "Radiant"
            elif tbr >= cr:
                return "Dire"
        return -1

        # r = 0 
        # d = 0
        # for i in range(len(senate)):
        #     if senate[i] == "R":
        #         r+=1
        #     else:
        #         d+=1
        #     queue.append(senate[i])



        # while queue:
        #     print(queue)
        #     val = queue.popleft()
        #     if not queue:
        #         if val == "R":
        #             return "Radiant"
        #         else:
        #             return "Dire"
        #     elif val == "R":
        #         if queue and queue[-1] == "D":
        #             queue.pop()
        #             queue.append(val)
        #         elif queue and queue[-1] == "R":
        #             count = 0
        #             found = False
        #             while queue:
        #                 if queue and queue[-1]=="R":
        #                     queue.pop()
        #                     count += 1
        #                 elif queue and queue[-1]=="D":
        #                     queue.pop()
        #                     found = "True"
        #                     for i in range(count):
        #                         queue.append("R")
        #                     queue.append(val)
        #                     break
        #             if found == False:
        #                 return "Radiant"
        #     elif val == "D":
        #         if queue and queue[-1] == "R":
        #             queue.pop()
        #             queue.append(val)
        #         elif queue and queue[-1] == "D":
        #             count = 0
        #             found = False
        #             while queue:
        #                 if queue and queue[-1]=="D":
        #                     queue.pop()
        #                     found = True
        #                     count += 1
        #                 elif queue and queue[-1]=="R":
        #                     queue.pop()
        #                     for i in range(count):
        #                         queue.append("D")
        #                     queue.append(val)
        #                     break
        #             if found == False:
        #                 return "Dire"
                    
                





        

