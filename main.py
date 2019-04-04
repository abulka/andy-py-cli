import os, glob
import requests

print("A simple test python app")
for i in range(200):
    print(f"{i} ", end=" ")
print()

print(os.listdir("."))
print(glob.glob("*.py"))
print(os.getcwd())
response = requests.get("http://www.google.com")
print(f"got {len(response.text)} chars from google.com")
print("done.")

