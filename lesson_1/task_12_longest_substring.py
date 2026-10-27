def longest_substring(s):
    max_len = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j - i + 1)
    return max_len

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))    
print(longest_substring("pwwkew"))   
