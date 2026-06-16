# import requests

# url = "https://jsonplaceholder.typicode.com/users/1"

# response = requests.get(url)
# data = response.json() 

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()


print(data[0]) 
print("Title:", data[0]['title'])
print("Body:", data[0]['body'])

for post in data:
    print(f"Title : {post['title']}")[10, 20, 30, 40, 50]