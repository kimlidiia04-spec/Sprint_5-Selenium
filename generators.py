import random

def generate_email():
    number = random.randint(100, 999)
    return f"lidia_kim_51_{number}@yandex.ru"

def generate_password():
    return f"{random.randint(100000, 999999)}"
