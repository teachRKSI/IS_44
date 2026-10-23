def length_of_longest_substring(s: str) -> int:
    """
    Возвращает длину самой длинной подстроки без повторяющихся символов.
    Используется алгоритм скользящего окна.
    """
    char_index = {}
    max_length = 0
    left = 0

    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

if __name__ == "__main__":
    print("Пример 1:", length_of_longest_substring("abcabcbb"))
    print("Пример 2:", length_of_longest_substring("bbbbb"))
    print("Пример 3:", length_of_longest_substring("pwwkew"))
