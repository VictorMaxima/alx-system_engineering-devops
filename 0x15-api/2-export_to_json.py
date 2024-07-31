#!/usr/bin/python3
'''A script that gathers employee name completed
tasks and total number of tasks from an API
'''

import re
import requests
import sys
import csv
import json


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
            task_all = [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": emp_name
            } for task in tasks]
            result = {str(id): task_all}
            with open(f"{id}.json", "w", encoding="utf8") as file:
                json.dump(result, file)
