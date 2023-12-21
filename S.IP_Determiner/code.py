IPV4 = "IPv4"
IPV6 = "IPv6"
ERROR = "Error"
good_syms = set('0123456789abcdefABCDEF')


def check_number_to_ip4(number: str) -> bool:
    if not number.isdigit() or int(number) > 255 or (number[0] == '0' and len(number) > 1):
        return False
    return True


def check_number_to_ip6(number: str, good_syms: set = good_syms) -> bool:
    return 0 < len(number) < 5 and all((sym in good_syms for sym in number))


# return IPV4, IPV6 or ERROR constant
def check_ip_address(ip_to_check: str) -> str:
    if '.' in ip_to_check:
        s = ip_to_check.split('.')
        if len(s) == 4 and all(map(check_number_to_ip4, s)):
            return IPV4
    if ':' in ip_to_check:
        s = ip_to_check.split(':')
        if len(s) == 8 and all(map(check_number_to_ip6, s)):
            return IPV6
    return ERROR


ip_to_check = input()
print(check_ip_address(ip_to_check))
