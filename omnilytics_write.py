#!/usr/bin/python3
"""
Generate 10 MB file, with random alphabetical string, real  number, inetegers, alphanumerics object.
this script run using python3
"""

import random
import string
import os
import sys


def gen_random_length(min_length=None, max_length=None) -> int:
    """
    Generate random length with fault min=5 and max=20
    """
    if not min_length:
        min_length = 5

    if not max_length:
        max_length = 20
    return random.randint(min_length, max_length)


def random_space() -> str:
    """
    Generate random space between 1-10 for alphanumerics
    """
    return " " * gen_random_length(min_length=1, max_length=10)


def random_int(length):
    """
    Generate random integer with max value
    """
    return "".join(random.choice(string.digits[1:]) for _ in range(length))


def random_alpahabetical_string(length):
    """
    Generate random alphabetical with specific length
    """
    return "".join(
        random.choice(string.ascii_lowercase) for _ in range(length)
    )


def random_alphanumerics(length):
    """
    Generate random alphanumerics based on length with extra space
    """
    output = "".join(
        random.choice(string.ascii_lowercase + string.digits) for i in range(length)
    )
    return random_space() + output + random_space()



def random_float(length):
    """
    Generate random real numbers based on length
    """
    return "{}".format(round(random.uniform(0.1, 1000000), length))


def generate_random_data_type() -> str:
    """
    Generate random data type with random length
    """
    char_gen_list = [
        random_alphanumerics, random_alpahabetical_string, random_float
    ]
    data_type = random.choice(char_gen_list)
    return data_type(gen_random_length())


def main(file_name="out_file.txt"):
    data = ""

    max_data = 10485760

    integer_data_length = max_data//2
    integer_data = []
    int_length = 0

    while int_length < integer_data_length:
        int_obj = random_int(gen_random_length(5, 20))
        int_length += len(int_obj) + 1
        integer_data.append(int_obj)

    non_integer = []
    non_integer_length = 0

    while non_integer_length < 10485760//2:
        obj_to_write = generate_random_data_type()
        non_integer_length += len(obj_to_write) + 1
        non_integer.append(obj_to_write)


    all_data = integer_data + non_integer

    random.shuffle(all_data)
    all_data = ','.join(all_data)
    with open(file_name, "w") as out_file:
        out_file.write(all_data)
        
    print(f"Generated file: {file_name}")
    print(f"File size: {os.stat(file_name).st_size}")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        file_name = "out.txt"
    main(file_name)


