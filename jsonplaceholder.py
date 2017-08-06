 # -*- coding : utf-8 -*-

import requests

url_resources = "https://jsonplaceholder.typicode.com/todos/"
url_resource = "https://jsonplaceholder.typicode.com/todos/{identifier}"

def get_task(identifier):
	resource = url_resource.format(identifier=identifier)
	return requests.get(resource)

def create_task(name):

	data = {
		"userId":1,
		"title":name,
		"completed":False
	}

	response = requests.post(url_resources,data=data)

	return response

def delete_task(identifier):

	resource = url_resource.format(identifier=identifier)
	response = requests.delete(resource)

	return response


def show_infos(task):
	print("Task name: {}".format(task.get("title")))
	print("Task status: {}".format(task.get("completed")))


if __name__ == "__main__":

	print("CREATING TASK...\n")

	task = create_task("New task").json()

	show_infos(task)

	task = get_task(1).json()

	print("\nRETURNED TASK:\n")

	show_infos(task)

	print("\nDELETING TASK...\n")

	task = delete_task(1)

	print(task.json())

