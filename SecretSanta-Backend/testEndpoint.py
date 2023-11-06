import requests
import json

# Define the URL of your Flask app
app_url = "http://localhost:5000/process_names"  # Change this URL to match your Flask app's URL

# Sample list of names
names = ["John", "Alice", "Bob"]

# Create a JSON payload with the list of names
payload = {"names": names}
print(json.dumps(payload))
# Make a POST request to the endpoint
response = requests.post(app_url, json=payload)

if response.status_code == 200:
    shuffled_names = response.json()
    print("Shuffled Names:", json.dumps(shuffled_names, indent=4))
else:
    print("Error:", response.status_code, response.text)