def generate_sequences(n, res=None, parenthesis_open=0, parenthesis_closed=0, bracket_open=0, bracket_closed=0):
    if not res:
        res = []
    if n % 2:
        print(*res)
    else:
        if len(res) < n:
            if parenthesis_open + bracket_open < n // 2:
                if bracket_open == bracket_closed:
                    generate_sequences(n, res+['('], parenthesis_open+1, parenthesis_closed, bracket_open, bracket_closed)
                generate_sequences(n, res + ['['], parenthesis_open, parenthesis_closed, bracket_open+1, bracket_closed)
            if parenthesis_closed < parenthesis_open and bracket_open == bracket_closed:
                generate_sequences(n, res + [')'], parenthesis_open, parenthesis_closed+1, bracket_open, bracket_closed)
            if bracket_closed < bracket_open:
                generate_sequences(n, res + [']'], parenthesis_open, parenthesis_closed, bracket_open, bracket_closed+1)
        else:
            print(*res, sep='')


n = int(input())
generate_sequences(n)
