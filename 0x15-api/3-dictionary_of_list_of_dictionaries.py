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


def user_dict_format(employee_id):
    """get formated user data"""
    data = get_data(employee_id)

    res = [
        {"username": data[0], "task": title, "completed": completed}
        for title, completed in data[1]
    ]

    return {employee_id: res}


def main():
    """main function"""
    all_users = requests.get("https://jsonplaceholder.typicode.com/users/")
    user_count = len(all_users.json())

    records = {x: user_dict_format(x) for x in range(1, user_count + 1)}

    with open("todo_all_employees.json",
              "w", encoding="utf-8") as file:
        json.dump(records, file)


if __name__ == "__main__":
    main()
