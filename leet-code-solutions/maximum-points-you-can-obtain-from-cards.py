class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        summ = sum(cardPoints[:n-k])
        minn = summ
        for r in range(n-k, n):
            summ += cardPoints[r]
            summ -= cardPoints[r-(n-k)]
            minn = min(minn, summ)
        return sum(cardPoints)-minn



        