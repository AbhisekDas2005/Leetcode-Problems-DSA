class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        available = {}
        for ch in letters:
            available[ch] = available.get(ch, 0) + 1

        def solve(index, available, current_score):
            if index==len(words):
                return current_score
            skip=solve(index + 1, available.copy(), current_score)
            word=words[index]
            newavailable = available.copy()
            word_score = 0
            possible = True
            for ch in word:
                if newavailable.get(ch, 0)==0:
                    possible = False
                    break
                newavailable[ch]-=1
                word_score+=score[ord(ch) - ord('a')]
            if possible:
                take = solve(
                    index + 1,
                    newavailable,
                    current_score + word_score
                )
            else:
                take = 0
            return max(skip, take)
        return solve(0, available, 0)