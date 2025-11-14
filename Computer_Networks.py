# Using code -> Network Call 
import requests

print("Python code to make an HTTP GET request")

r = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print("Status :", r.status_code)
print("Headers :", r.headers)
print("Body :", r.text[:20], "...")