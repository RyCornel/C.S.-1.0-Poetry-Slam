def get_file_lines():
    filename = open("E.E.Cummings.txt", "r")
    content_list = filename.readlines()
    filename.close()
    print(content_list)
    

get_file_lines()



