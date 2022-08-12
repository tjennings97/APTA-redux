import pwd
import random
import string
from passlib.context import CryptContext

# telling passlib what hashing algorithm we want to use - bcrypt in this case
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") 

# from https://pynative.com/python-generate-random-string/
# get random password pf length 8 with letters, digits, and symbols
def random_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(8))
    return password

def hashed_password(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)