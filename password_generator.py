import random
import string
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Print primary text in purple and password in green
print(Fore.MAGENTA + "Your random password is: " + Fore.GREEN + generate_password())
