def read(file_name):
    #this function read a file line by line and return list contain lines
    with open(file_name, "r") as file:
        lines = file.readlines()
    return lines

def sum(name):
    doc = read(name)[0]
    signs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
              'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
              's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             '{', '}', ':', ',', '"', '[', ']', ]
    for sign in signs:
        doc = doc.replace(sign, ' ')
    numbers = doc.split()
    n=0
    for number in numbers:
        n += int(number)
    return n



print(sum('skychallenge_accounting_input.txt'))