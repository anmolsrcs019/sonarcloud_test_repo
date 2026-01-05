def normalize_username(username: str) -> str:
    if not username:
        raise ValueError("Username cannot be empty")
    return username.strip().lower()