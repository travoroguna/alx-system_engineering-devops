#!/usr/bin/python3
"""script that fetches data using an api"""

import csv
import requests
import sys


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

    res = [[sys.argv[1], data[0], str(status), task]
           for task, status in data[1]]
    res = [["{}".format(y) for y in x] for x in res]

    with open(str(sys.argv[1])+".csv", 'w', encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(res)


if __name__ == "__main__":
    main()
