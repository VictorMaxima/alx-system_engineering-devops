#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import re
import requests
import sys
import csv


REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            id = int(sys.argv[1])
            emp_req = requests.get('{}/users/{}'.format(REST_API, id)).json()
            task_req = requests.get('{}/todos'.format(REST_API)).json()
            emp_name = emp_req.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, task_req))
            completed_tasks = list(filter(lambda x: x.get('completed'), tasks))
            with open(f"{id}.csv", "w", newline='') as file:
                writer = csv.writer(file, quotechar='\"',
                                    quoting=csv.QUOTE_ALL)
                for task in tasks:
                    writer.writerow([id, emp_name,
                                    task.get('completed'), task.get("title")])
