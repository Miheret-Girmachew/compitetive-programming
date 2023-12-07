class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        array = []
        string = 0
        for num in spaces:
            array.append(s[string:num])
            array.append(" ")
            string = num
        array.append(s[string:])
        return "".join(array)