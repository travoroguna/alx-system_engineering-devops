#!/usr/bin/python3
"""script that fetches data using an api"""

import sys
import requests


EMPLOYEE_DATA = 'https://jsonplaceholder.typicode.com/users/{}'
EMPLOYEE_TODOS = 'https://jsonplaceholder.typicode.com/users/{}/todos'


def parse_todos(emp_todos):
    """parses employee todos"""

    emp_todos = emp_todos.json()

    total = len(emp_todos)
    tasks = [x["title"] for x in emp_todos if x["completed"]]

    return tasks, len(tasks), total


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

    tasks, completed, total = parse_todos(emp_todos)

    return name, completed, total, tasks


def main():
    """main function"""
    if len(sys.argv) != 2:
        quit()

    data = get_data(sys.argv[1])
    print_data(*data)


if __name__ == "__main__":
    main()
