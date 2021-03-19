#!/usr/bin/python
"""
Read the input file and determine the object type
"""

import sys
from queue import Queue
from threading import Thread


queue = Queue() 


def process_data(obj_data):
    summary = {
        "int": 0,
        "alphanum": 0,
        "string": 0,
        "real_num": 0,
        "data": [],
        "total": 0
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
        summary['data'].append(f"{obj} - {obj_type}")
        summary['total'] += 1
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
    
    result = process_data(row.split(","))
    print("\n".join(result['data']))
    total = result['total']
    print()
    print("#" * 20)
    print(f"Integer Data: {round((result['int']/total) * 100, 2)} %")
    print(f"Alphanumeric Data: {round((result['alphanum']/total) * 100, 2)} %")
    print(f"String Data: {round((result['string']/total) * 100, 2)} %")
    print(f"Real Numbers Data: {round((result['real_num']/total) * 100, 2)} %")
                    

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        file_name = sys.argv[1]
    else:
        file_name = "out.txt"
    main(file_name)
