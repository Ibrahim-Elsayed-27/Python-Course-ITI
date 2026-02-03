import re

def check_email(email: str, email_regex: str) -> bool:
    return bool(re.fullmatch(email_regex, email))
