class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        formed = 0
        left = 0

        min_len = float('inf')
        best_start = 0

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            if c in need and window[c] == need[c]:
                formed += 1

            while formed == len(need):
                current_len = right - left + 1

                if current_len < min_len:
                    min_len = current_len
                    best_start = left

                c = s[left]

                if c in need and window[c] == need[c]:
                    formed -= 1

                window[c] -= 1
                left += 1

        if min_len == float('inf'):
            return ""

        return s[best_start:best_start + min_len]