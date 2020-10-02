def get_file_lines():
    filename = open("E.E.Cummings.txt", "r")
    content_list = filename.readlines()
    for i in content_list:
        print(i)
    filename.close()
    
get_file_lines()


def lines_printed_backwards():
    filename = open("E.E.Cummings.txt", "r")
    content_list = filename.readlines()
    for i in reversed(content_list):
        print(i)
    filename.close()


lines_printed_backwards()

import random

def lines_printed_random():
    filename = open("E.E.Cummings.txt", "r")
    lines_list = filename.readlines()
    random_poem = random.sample(lines_list, len(lines_list))
    for x in random_poem:
        print(x)
    filename.close()

lines_printed_random()




