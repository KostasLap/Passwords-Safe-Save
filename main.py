import random

my_psw = {}

def passwordsaver():
    state = input("Do you need to save your password? (Yes or No): ")

    if state.lower() == "yes":
        key = input("Enter platform: ")
        value = input("Enter password: ")
        my_psw[key] = value
        print(my_psw)
        return passwordsaver()

    else:
        converter_of_psw()
        print((my_psw))
        print("Goodbye")

def converter_of_psw():
    character1 = (1, "q", 5, "k", "@", "Q", "K")
    character2 = (3, 9, "a", "!", "f", "A", "F")

    for key, value in my_psw.items():
        new_psw = []
        for char in value:
            if (len(value) + 11) % 2 == 0:
                char = str(char) + str(random.choice(character1))
                new_psw.append(char)
            else:
                char = str(char) + str(random.choice(character2))
                new_psw.append(char)
        new_value = "".join(new_psw)
        my_psw[key] = new_value
    save_to_file(my_psw, 'passwords.txt')

def save_to_file(dictionary, filename):
    with open(filename, 'w') as f:
        for key, value in dictionary.items():
            f.write(f"{key}: {value}\n")


def reverse_converter_of_psw():
    filename = input("Enter the filename: ")
    my_psw = open_file(filename)
    if my_psw:
        for key, value in my_psw.items():
            new_value = value[::2]
            my_psw[key] = new_value
        print("YOUR PASSWORS ARE:", my_psw)

def open_file(filename):
    try:
        with open(filename, 'r') as f:
            my_dict = {}
            for line in f:
                key, value = line.strip().split(': ')
                my_dict[key] = value
            return my_dict
    except FileNotFoundError:
        print("File not found.")
        return None




























