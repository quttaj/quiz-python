import requests

response = requests.get(
    "https://opentdb.com/api.php",
    params={"amount": 10},
    timeout=20
)
response.raise_for_status()

data = response.json()

if data.get("response_code") != 0 or not data.get("results"):
    raise RuntimeError(
        f"Failed to load questions. "
        f"Server response: {data}. "
        f"Please wait a moment and try again."
    )

question_data = data["results"]