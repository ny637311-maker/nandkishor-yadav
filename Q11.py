import requests
from  import BeautifulSoup
import json

try:
    url = "http://quotes.toscrape.com"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        quotes_data = []

        quotes = soup.find_all("div", class_="quote")

        for q in quotes:
            text = q.find("span", class_="text").get_text()
            author = q.find("small", class_="author").get_text()

            quotes_data.append({
                "quote": text,
                "author": author
            })

    
        print("Quotes by Albert Einstein:\n")
        for item in quotes_data:
            if item["author"] == "Albert Einstein":
                print(item["quote"])
                print("-" * 40)

        
        with open("quotes.json", "w") as file:
            json.dump(quotes_data, file, indent=4)

       
        print("\nTotal quotes scraped:", len(quotes_data))

    else:
        print("Failed to fetch webpage. Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Request error:", e)

except Exception as e:
    print("An error occurred:", e)