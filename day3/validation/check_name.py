def check_name(name: str) -> bool:
    name = name.strip()
    if len(name) < 3:
        return False
    return name.replace(" ", "").isalpha()
