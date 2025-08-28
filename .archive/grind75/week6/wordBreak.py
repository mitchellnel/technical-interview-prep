from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[i] is True if there is a word in the dictionary that ends at ith index of s
        #   AND dp is also True at the beginning of the word
        dp = [False for _ in range(len(s))]

        for idx, char in enumerate(s):
            for word in wordDict:
                if word == s[idx - len(word) + 1 : idx + 1] and (
                    dp[idx - len(word)] or (idx - len(word) == -1)
                ):
                    dp[idx] = True

        return dp[-1]


def main():
    soln = Solution()

    print(
        f's = "leetcode", wordDict = ["leet","code"] --> {soln.wordBreak("leetcode", ["leet","code"])}'
    )
    print(
        f's = "applepenapple", wordDict = ["apple","pen"] --> {soln.wordBreak("applepenapple", ["apple","pen"])}'
    )
    print(
        f's = "catsandog", wordDict = ["cats","dog","sand","and","cat"] --> {soln.wordBreak("catsandog", ["cats","dog","sand","and","cat"])}'
    )


main()
