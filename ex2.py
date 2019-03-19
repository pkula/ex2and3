def read(file_name):
    #this function read a file line by line and return list contain lines
    with open(file_name, "r") as file:
        passwords = file.readlines()
    return passwords


def is_val_one_password(password):
    words = password.split()
    for word in words:
        if words.count(word) != 1:
            return False
    return True

def validator(name):
    passwords = read(name)
    n = 0
    for password in passwords:
        n = n+1 if is_val_one_password(password) else n
    return n

