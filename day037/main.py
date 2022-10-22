import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "ah980v98np9a8nsdv",
    "username": "rrohde",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
