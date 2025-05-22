import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
print(response.text)

for i in range(0, 3):
    print(response.json()[i]['name'])