# API Fetcher in Python using requests

import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        # Check if the response is successful (status code 200-299)
        if response.status_code == 200:
            data = response.json()  # Parse JSON data
            print(data)  # Log the data or handle it accordingly
        else:
            print(f"Error fetching data: {response.status_code}")
    except Exception as e:
        print(f"There was an error: {e}")

# Example usage
api_url = 'https://jsonplaceholder.typicode.com/posts'  # Replace with your API URL
fetch_data(api_url)
