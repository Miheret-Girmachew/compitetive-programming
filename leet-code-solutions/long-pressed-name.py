class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """
        ss=set(name)
        ss1=set(typed)
        print(ss)
        print(ss1)
        if ss != ss1:
            return False
        hashh = {}
        hashh1 = {}
        for i in range(len(name)):
            hashh[name[i]]=hashh.get(name[i],0)+1
        for i in range(len(typed)):
            hashh1[typed[i]]=hashh1.get(typed[i],0)+1 
        for i in range(len(name)):
            if hashh[name[i]] >hashh1[name[i]]:
                return False
        return True
        """
        name = list(name)
        typed = list(typed)
        if name[0] != typed[0]:
            return False
        i = 1
        j = 1
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            elif name[i-1] == typed[j]:
                j += 1
            else:
                return False
        while j < len(typed):
            if name[i-1] == typed[j]:
                j += 1
            else:
                return False
        return i == len(name)