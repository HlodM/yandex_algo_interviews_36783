def string_matches_template(s: str, template: str) -> bool:
    i = j = 0
    last_match = 0
    star = -1

    while i < len(s):
        if j < len(template) and template[j] in {s[i], "?"}:
            i += 1
            j += 1
        elif j < len(template) and template[j] == "*":
            last_match = i
            star = j
            j += 1
        elif star != -1:
            last_match += 1
            i = last_match
            j = star + 1
        else:
            return False

    while j < len(template) and template[j] == "*":
        j += 1

    return j == len(template)


template = input()
string_to_check = input()
if string_matches_template(string_to_check, template):
    print('YES')
else:
    print('NO')
