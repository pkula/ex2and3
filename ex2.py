def read(file_name):
    #this function read a file line by line and return list contain lines
    with open(file_name, "r") as file:
        passwords = file.readlines()
    return passwords

def validator(name):
    passwords = read(name)
    n = 0
    is_bad_password = False
    for password in passwords:
        words = password.split()
        for i in range (0,len(words)-1):
            for w in range(i+1,len(words)):
                if words[i].strip() == words[w].strip():
                    is_bad_password = True
        if is_bad_password:
            is_bad_password = False
        else:
            n+=1
    return n



