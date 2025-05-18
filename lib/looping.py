#!/usr/bin/env python3
def happy_new_year():
    count = 10
    # code goes here!
    while count >=1:
        print(count)
        count -= 1
    print("Happy New Year!")

happy_new_year()


def square_integers(int_list):
    # code goes here!
    return [i * i for i in int_list]
print(square_integers([1, 2, 3, 4, 5]))

def squared_integers(int_list):
    # code goes here!
    # print(int_list)
    square = [integer * integer for integer in int_list]
    # print(square)
    return square
print(squared_integers([1, 2, 3, 4, 9]))

""" def fizzbuzz():
    # code goes here!
    results = []
    count = 1
    # for count in range(1,101):
    while count <= 100:
        if count% 3 == 0 and count%5 == 0: 
            results.append("FizzBuzz")
        elif count % 3 == 0:
            results.append("Fizz")
        elif count % 5 == 0:
            results.append("Buzz")
        else:
            results.append(count)
        count +=1
    return results 
print(fizzbuzz()) """

def fizzbuzz():
    for i in range(1, 101):
        if i% 3 == 0 and i%5 == 0: 
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizzbuzz()
        


player_heights = [0.008, 0.008, 0.008, 0.009, 0.008, 0.01, 0.009, 0.009, 0.01, 0.008, 0.009, 0.009, 0.008, 0.008, 0.008, 0.009, 0.008, 0.009, 0.01, 0.01]
# inch_heights = list()
# for height in player_heights:
#     inch_height = height * 7920
#     inch_heights.append(inch_height)
# print(inch_heights)

# inch_heights = [height * 7920 for height in player_heights]
# print(inch_heights)

player_heights = [height * 7920 for height in player_heights]
print(player_heights)