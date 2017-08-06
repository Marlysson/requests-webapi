import json
import requests

class Github:

	def __init__(self,token):
		self.token = token
		self.api_github = "https://api.github.com"

		self.urls = {
			"infos_user" : "/users/{username}", # GET
			"create_repo" : "/user/repos", # POST
			"delete_repo" : "/repos/{owner}/{repository}", # DELETE
		}

		self.header_autorization = {"Authorization":"token {}".format(token)}

	def __formatted_url(self,endpoint,data=None):

		action = self.urls.get(endpoint,None)

		formatted_url = self.api_github + action

		if data:
			formatted_url = formatted_url.format(**data)

		return formatted_url

	def info_user(self,username):

		endpoint_user = self.__formatted_url("infos_user",{"username":username})

		return requests.get(endpoint_user).json()

	def create_repo(self,repository_name):

		data = json.dumps({"name":repository_name})

		endpoint_create_repo = self.__formatted_url("create_repo")
	
		response = requests.post(endpoint_create_repo,
						data=data,
						headers=self.header_autorization
					)

		return response

	def delete_repo(self, owner, repository_name):
		
		repository = repository_name.replace(" ","-")

		data = {
			"owner":owner,
			"repository":repository
		}

		formatted_url = self.__formatted_url("delete_repo",data)

		response = requests.delete(formatted_url,
							headers=self.header_autorization)

		return response

if __name__ == "__main__":

	github = Github("YOUR_GITHUB_TOKEN")

	print("USER INFORMATIONS: \n")

	print(github.info_user("Marlysson"))

	print("CREATING A REPOSITORY: \n")

	dados = github.create_repo("Novo")

	print(dados.headers.get("Status"))
	print(dados.json().get("html_url"))