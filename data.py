import requests

AMOUNT = 10

parameters = {
    "amount": AMOUNT,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]