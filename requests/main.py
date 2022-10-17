import requests

response = requests.post("https://petstore.swagger.io/v2/pet",json ={
  "id": 777,
  "category": {
    "id": 0,
    "name": "camell"
  },
  "name": "camell",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "camell"
    }
  ],
  "status": "available"
}) 
print(response.text)


response = requests.post("https://petstore.swagger.io/v2/pet",json ={
  "id": 777,
  "category": {
    "id": 0,
    "name": "Spider"
  },
  "name": "Spider",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "Spider"
    }
  ],
  "status": "available"
}) 
print(response.text)


response = requests.get("https://petstore.swagger.io/v2/pet/777")
print(response.text)