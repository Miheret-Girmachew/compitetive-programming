class Solution:
    def numberOfWays(self, s: str) -> int:
        ones = 0
        zeros = 0
        zero_ones = 0
        one_zeros = 0
        result = 0
        for i in s:
            if i == "1":
                ones+=1
                zero_ones+=zeros
                result+=one_zeros
            else:
                zeros+=1
                one_zeros+=ones
                result+=zero_ones
        return result


            


        