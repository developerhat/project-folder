#Practicing using API's 06/06/21

import requests

random_user = requests.get("https://api.thedogapi.com/v1/breeds")

print(random_user.text)
