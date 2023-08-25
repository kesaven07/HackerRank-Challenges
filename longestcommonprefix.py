class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        maxLen = 0
        minStr = min(strs, key=len)
        for i, char in enumerate(minStr):
            for string in strs:
                if string[i]!=char:
                    return minStr[:maxLen]
                
            maxLen+=1
            
        return minStr[:maxLen]