import requests
url="https://api.spacexdata.com/v4/launches/past"
print("ssssssss")
response=requests.get(url)
response.json()
data=pd.json_normalize(response.json())
