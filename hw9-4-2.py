# author: LM (AMDG) 1/17/22
def products(list_numbers, number):
    new_lst = []
    for index in list_numbers:
        new_value = index * number
        new_value= new_lst.append(new_value)
        print(new_lst)

products([1, 2, 3, 4], 9)