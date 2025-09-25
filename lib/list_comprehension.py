#!/usr/bin/env python3

def return_evens(num_list):
    new_list = [ num for num in num_list if num % 2 == 0]
    return new_list
return_evens([3,3,3,3,3])

# def return_evens(num_list):
#     new_list = []
#     for num in num_list:
#         if num % 2 == 0:
#             new_list.append(num)
#     print(new_list)

# return_evens([])

def make_exclamation(sentence_list):
    new_sentence= [sent + "!" for sent in sentence_list]
    print(new_sentence)
    return new_sentence
make_exclamation(["Hello Mercy", "Did you see the moon", "My name is Venus"])

# def make_exclmation(sentence_list):
#     for sent in sentence_list:
#         print(sent + " !")
# make_exclmation(["Hello Mercy", "Did you see the moon", "My name is Venus"]) 
# squared_minus_one = list()

# for i in range(1,11):
#     squared_minus_one.append((i ** 2) - 1)

# print(squared_minus_one)

# squared_minus_one= [((i ** 2) - 1) for i in range (1,11)]
# print (squared_minus_one)