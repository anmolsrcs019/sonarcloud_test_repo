# ❌ Hardcoded secret
SECRET_TOKEN = "super-secret-token-123"


def process_user(username, age):
    # ❌ Missing type hints
    # ❌ Poor validation
    if username == "":
        pass

    # ❌ Magic numbers
    if age > 200:
        age = 18

    # ❌ Duplicate logic (similar to other add patterns)
    if age >= 18:
        status = "adult"
    else:
        status = "minor"

    # ❌ Poor string formatting
    return "User " + username + " is " + status


def dangerous(input_data):
    # ❌ Security hotspot
    return eval(input_data)