class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ''.join(map(str, digits))
        num = int(string) + 1
        string = str(num)
        result = list(map(int, string))
        return result

          
        