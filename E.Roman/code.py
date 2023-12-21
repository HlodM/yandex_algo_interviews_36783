def convert_to_arabic(s: str) -> int:
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    ans, count_in_row = 0, 0
    used_chars = set()

    for idx in range(len(s)):
        if s[idx] in ('V', 'L', 'D'):
            if s[idx] in used_chars:
                return -1
            else:
                used_chars.add(s[idx])
        elif idx and s[idx] == s[idx - 1]:
            count_in_row += 1
        else:
            count_in_row = 0
        if count_in_row > 2 or s[idx] not in roman:
            return -1
        if idx < len(s) - 1:
            if roman[s[idx]] < roman[s[idx + 1]]:
                if roman[s[idx + 1]] // roman[s[idx]] not in (5, 10) or count_in_row:
                    return -1
                else:
                    ans -= 2 * roman[s[idx]]
        ans += roman[s[idx]]

    return ans


roman_number = input()
print(convert_to_arabic(roman_number))
