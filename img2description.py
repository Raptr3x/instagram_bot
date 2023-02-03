import requests

url = "https://describe-image-content-api.p.rapidapi.com/api/v1/describe_image"

querystring = {"image_url":"https://scontent-vie1-1.cdninstagram.com/v/t51.2885-15/116336732_1003207993470070_3363504100969961476_n.jpg?stp=dst-jpg_e15&_nc_ht=scontent-vie1-1.cdninstagram.com&_nc_cat=110&_nc_ohc=Bnwe4iyaZ0gAX-gFi-t&tn=Q1lNAMYEBz3RqLbc&edm=ACWDqb8BAAAA&ccb=7-5&ig_cache_key=MjM2MzIyMzU4MDE3NDM2OTk0NA%3D%3D.2-ccb7-5&oh=00_AfDTbAjqf-MvceGjA0cY1m1oJBgnPoXqrCd4yQ0ZQutphA&oe=63E2089F&_nc_sid=1527a3"}

headers = {
	"X-RapidAPI-Key": "81909cbbb4mshe62505a92acd45ep13b91djsn584c557b4cb0",
	"X-RapidAPI-Host": "describe-image-content-api.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response)
print(response.text)