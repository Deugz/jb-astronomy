





def read_file(filename):
    with open(filename) as f:
        contents = f.read().splitlines()
    return contents


response_list = read_file("response_list.txt")

print(response_list)