import re
def validate_email(email):
    pattern='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern,email) and '..' not in email:
        return True
    else:
        return False

