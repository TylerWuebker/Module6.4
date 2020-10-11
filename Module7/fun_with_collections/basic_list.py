def make_list():
    i = 0
    for i in range(0,2):
        user_input = get_input()
        str(user_input);
        list.append(user_input)
    return list
def get_input():
    input = ''
    print("Please enter your input : ")
    input = input()
    return input

if __name__ == '__main__':
    make_list()
