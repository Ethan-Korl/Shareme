from random import randint

def generate_code() -> int:
    gr_code = randint(1000, 9999)
    return gr_code


def extract_name(email):
    parts = email.split('@')
    name = parts[0]
    return name
