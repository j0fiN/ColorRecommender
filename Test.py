import requests

res = requests.post(url="http://127.0.0.1:5000/api", json={"key":3, "note":"C"})
print(res.status_code)
print(res.content)