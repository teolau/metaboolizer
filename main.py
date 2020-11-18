import hashlib


# this function returns the hexadecimal 64-digit long, uncut password
def create_password(master_key, service):
    if not isinstance(master_key, str) or not isinstance(service, str):
        raise Exception("The master key and the service name must be strings")

    # join the service name and the master key
    salted_key = master_key.strip().lower() + service.strip().lower()

    # encode the resulting string into a byte object
    salted_key = str.encode(salted_key)

    for i in range(10000):
        encoded = hashlib.sha256(salted_key).hexdigest()
        salted_key = str(encoded).encode()

    return encoded


# transforms the hexadecimal into a string (71 chars pool)
def to_password(hexadecimal, length=16):
    if 1 > length > 64 or not isinstance(length, int):
        raise Exception("Length must be an integer between 1 and 64.")

    characters = []     # the pool of chars that the final password can contain
    password = ""
    decimal = int(hexadecimal, 16)

    # a-z
    for i in range(97, 123):
        characters += chr(i)

    # A-Z
    for i in range(65, 91):
        characters += chr(i)

    # 0-9
    for i in range(10):
        characters += str(i)

    # Special characters
    characters += ['!', '@', '#', '$', '&', '?', '.', '_', '-']

    for i in range(length):
        password += characters[decimal % 70]
        decimal //= 10      # cuts the last digit

    return password


while True:
    print("Insert the master key:")
    key = input()
    print("Insert the name of the service/site:")
    salt = input()
    print("Your password is: ", to_password(create_password(key, salt)))
    print("\n\n")
