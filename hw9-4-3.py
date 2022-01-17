# author: LM (AMDG) 1/17/22
def count_e(string):
    counter = 0
    for index, value in enumerate(string):
        if 'e' in value:
            counter += 1

        elif 'E' in value:
            counter += 1
 
    return counter

print(count_e(['eeeeee']))
