def check_password(password: str, min_length: int) -> bool:
    if not isinstance(password, str):
        return False
    return len(password) >= min_length
