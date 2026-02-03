import re

def check_phone(phone: str, phone_regex: str) -> bool:
    return bool(re.fullmatch(phone_regex, phone))
