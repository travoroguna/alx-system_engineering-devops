#!/usr/bin/env python3
"""script that fetches data using an api"""

import json
import sys

import requests

EMPLOYEE_DATA = 'https://jsonplaceholder.typicode.com/users/{}'
EMPLOYEE_TODOS = 'https://jsonplaceholder.typicode.com/users/{}/todos'


def parse_todos(emp_todos):
    """parses employee todos"""

    emp_todos = emp_todos.json()
    return [[x["title"], x["completed"]] for x in emp_todos]


def print_data(name, completed, total, todos):
    """prints employee data to stdout"""

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total))

    for todo in todos:
        print("\t {}".format(todo))


def get_data(employee_id):
    """gets employee data
        args:
            employee_id(int) - employee_id?

        Returns:
            (dict) employee data
    """

    emp_dat = requests.get(EMPLOYEE_DATA.format(employee_id))
    emp_todos = requests.get(EMPLOYEE_TODOS.format(employee_id))

    name = emp_dat.json()['name']

    tasks = parse_todos(emp_todos)

    return name, tasks


def main():
    """main function"""
    if len(sys.argv) != 2:
        quit()

    data = get_data(sys.argv[1])

    res = [
        {"task": title, "completed": completed, "username": data[0]}
        for title, completed in data[1]
    ]

    record = {sys.argv[1]: res}

    with open("{}.json".format(sys.argv[1]),
              "w", encoding="utf-8") as file:
        json.dump(record, file)


if __name__ == "__main__":
    main()
