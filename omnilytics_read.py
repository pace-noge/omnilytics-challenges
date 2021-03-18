#!/usr/bin/python
"""
Read the input file and determine the object type
"""

import sys
from queue import Queue
from threading import Thread


queue = Queue() 


def print_data(obj_data):
    summary = {
        "int": 0,
        "alphanum": 0,
        "string": 0,
        "real_num": 0
    }
    for obj in obj_data:
        if obj.isdigit():
            obj_type = "integer"
            summary["int"] += 1
        else:
            if " " in obj:
                obj_type = "alphanumeric"
                summary['alphanum'] += 1
                obj = obj.strip()
            else:
                if obj.isalpha():
                    obj_type = "alphabetical strings"
                    summary['string'] += 1

                else:
                    obj_type = "real numbers"
                    summary['real_num'] += 1
        # print(f"{obj} - {obj_type}")
    return summary


def main(file_name="out.txt"):
    integer_data = 0
    alphanumeric_data = 0
    alpha_data = 0
    real_number_data = 0
    total = 0
    threads_list = list()

    with open(file_name, "r") as in_file:
        row = in_file.readline()
        row = row.split(",")
    
    len_data = len(row)//4

    data = [row[x:x+len_data] for x in range(0, len(row), len_data)]

    for d in data:
        t = Thread(target=lambda q, arg1: q.put(print_data(arg1)), args=(queue, d))
        t.start()
        threads_list.append(t)
    
    for t in threads_list:
        t.join()

    result = {}
    while not queue.empty():
        result = queue.get()
    

    total = sum([result[i] for i in result])
    print()
    print("#" * 20)
    print(f"Integer Data: {(result['int']/total) * 100} %")
    print(f"Alphanumeric Data: {(result['alphanum']/total) * 100} %")
    print(f"String Data: {(result['string']/total) * 100} %")
    print(f"Real Numbers Data: {(result['real_num']/total) * 100} %")



    #     for obj in row:
    #         if obj.isdigit():
    #             obj_type = "integer"
    #             integer_data += 1
    #         else:
    #             if " " in obj:
    #                 obj_type = "alphanumeric"
    #                 alphanumeric_data += 1
    #                 obj = obj.strip()
    #             else:
    #                 if obj.isalpha():
    #                     obj_type = "alphabetical strings"
    #                     alpha_data += 1
    #                 else:
    #                     obj_type = "real numbers"
    #                     real_number_data += 1
    #         total += 1
    #         print(f"{obj} - {obj_type}")
                
    #         # if obj.startswith(" ") and obj.endswith(" "):
    #         #     obj_type = "alphanumeric"
    #         #     alphanumeric_data += 1
    #         # else:
    #         #     if obj.isdigit():
    #         #         obj_type = "integer"
    #         #         integer_data += 1
    #         #     elif obj.isalpha():
    #         #         obj_type = "alphabetical strings"
    #         #         alpha_data += 1
    #         #     else:
    #         #         obj_type = "real numbers"
    #         #         real_number_data += 1
            
    #         # total += 1        
    #         # print(f"{obj.strip()} - {obj_type}")
    # print("*" * 10)
    # print(f"Integer Data: {(integer_data/total) * 100}%")
    # print(f"Alphanumeric Data: {(alphanumeric_data/total) * 100}%")
    # print(f"String Data: {(alpha_data/total) * 100}%")
    # print(f"Real Numbers Data: {(real_number_data/total) * 100}%")
                    

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        file_name = "out.txt"
    main(file_name)
