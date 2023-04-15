import random


# csv reader
def csv_reader(file_name):
    return open(file_name, 'r')

# csv parser
def csv_parser(file_name, separator, column, row):
    new_string = ''
    new_list = ['' for i in range (row)]; new_list_counter = 0
    new_new_list = [['' for j in range (row)] for i in range (column)]; new_new_list_counter = 0
    for i in (file_name):
        for j in (i):
            if j != separator and j != '\n':
                new_string += j
            elif j == separator:
                new_list[new_list_counter] = new_string
                new_list_counter += 1
                new_string = ''
            else:
                new_list[new_list_counter] = new_string
                new_new_list[new_new_list_counter] = new_list
                new_string = ''
                new_list = ['' for i in range (row)]
                new_list_counter = 0
                new_new_list_counter += 1
    return new_new_list


# menyatukan 2 string
def combine(string1, string2):
    string1 += string2
    return string1

# split jika asumsikan hanya ada bondowoso + roro + 100 jin, karena ada 3 kolom maka total ada 102*3 = 306
def spllt(words, separator, n, m):
    new_list = ['' for i in range (m)]
    new_string = ''
    count = 0
    for j in range (n):
        if words[j] != separator and words[j] != '\n':
            new_string += words[j]
        elif words[j] == separator or words[j] == '\n':
            new_list[count] = new_string
            new_string = ''
            count += 1
    return new_list

# sorted
def sort(x, n):
    for i in range (n):
        for j in range (n):
            if x[j] > x[i]:
                x[j],x[i] = x[i],x[j]
    return x

# mengecek apa ada x dalam list
def check(list, x, n):
    verifier = False
    for i in range (n):
        if list[i] == x:
            verifier = True
    return verifier

# mengecek apa ada x dalam matrix
def checkm(list, x, m, n, p):
    verifier = False
    for i in range (n):
        for j in range (p, m):
            if list[j][i] == x:
                verifier = True
    return verifier

# length string
def str_len(x):
    return len(x)

# random
def randomize():
    return random.randint(0, 5)

# absolute
def abso(x):
    if x < 0:
        return x*(-1)
    else:
        return x