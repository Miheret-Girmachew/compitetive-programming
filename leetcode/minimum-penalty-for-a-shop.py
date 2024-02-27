class Solution:
    def bestClosingTime(self, customers: str) -> int:
        c = Counter(customers)
        after_y = 0

        hs = {} 
      
        if not c["Y"]:
            c["Y"] = 0
        elif not c["N"]:
            c["N"] = 0
        hs[c["N"]] = [len(customers)]


        for i in range(len(customers)-1, -1, -1):
            if customers[i] == "Y":
                val = 1 + after_y + c["N"]
                after_y += 1
                if not val in hs:
                    hs[val] = []
                hs[val].append(i)
            else:
                c["N"] -= 1
                val = after_y + c["N"]
                if not val in hs:
                    hs[val] = []
                hs[val].append(i)
        val = min(hs)
        hs[val].sort()
        return hs[val][0]
            



        