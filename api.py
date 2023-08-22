import requests
import json
# url= "http://api.weatherapi.com/v1/current.json?key=5a837c466a0c4af693f81704231306&q=Gurgaon"
url= "http://api.weatherapi.com/v1/current.json?key=5a837c466a0c4af693f81704231306&q="+input("enter city name")

df = requests.get(url)
data=json.loads(df.content)
print(data['location']['region'])
# print(data['location']['region'])
print(data['location'])
print(df.content)


