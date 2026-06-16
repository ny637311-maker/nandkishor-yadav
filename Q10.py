import requests
import json

try:
    
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)

   
    if response.status_code == 200:
        users = response.json()

        
        print("User Details:\n")
        for user in users:
            print("Name:", user.get("name"))
            print("Email:", user.get("email"))
            print("Phone:", user.get("phone"))
            print("-" * 30)

        
        with open("users.json", "w") as file:
            json.dump(users, file, indent=4)

       
        print("Total users fetched:", len(users))

    else:
        print("Failed to fetch data. Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred while making API request:", e)

except json.JSONDecodeError:
    print("Error decoding JSON response")

except Exception as e:
    print("An unexpected error occurred:", e)