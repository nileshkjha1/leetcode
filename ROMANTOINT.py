class Solution:
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        answer = 0

        for i in range(len(s) - 1):
            if values[s[i]] < values[s[i + 1]]:
                answer -= values[s[i]]
            else:
                answer += values[s[i]]

        answer += values[s[-1]]

        return answer