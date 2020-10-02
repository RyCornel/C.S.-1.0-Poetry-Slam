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
