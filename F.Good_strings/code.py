def convert_to_good_string(probably_bad_string: str) -> str:
    stack = []
    for symbol in probably_bad_string:
        if stack and stack[-1].lower() == symbol.lower() and stack[-1] != symbol:
            stack.pop()
        else:
            stack.append(symbol)
    return "".join(stack)


probably_bad_string = input()
print(convert_to_good_string(probably_bad_string))
