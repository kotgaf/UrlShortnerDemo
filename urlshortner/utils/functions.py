import random
import string


def generate_random_string(length=10):
    result = ''
    for i in range (1, length+1):
        result += random.choice(string.ascii_letters + string.digits)
    return result
