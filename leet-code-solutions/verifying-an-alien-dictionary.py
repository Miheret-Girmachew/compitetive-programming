class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            j = 0
            while j < len(word1) and j < len(word2):
                if order.index(word1[j]) > order.index(word2[j]):
                    return False
                elif order.index(word1[j]) < order.index(word2[j]):
                    break
                j += 1

            if j == len(word2) and j < len(word1):
                return False

        return True