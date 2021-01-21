import requests

BASE = "http://127.0.0.1:5000/"

#masukin data manual
#response = requests.put(BASE + "video/3" , {"likes": 100, "name": "Fozi", "views": 100} )
#print(response.json())

#mengganti data manual
#response = requests.patch(BASE + "video/2", {"views": 99, "likes":101})
#print(response.json())

#melihat data semua
response = requests.get(BASE + "video/2")
print(response.json())

#hapus data manual
#response = requests.delete(BASE + "video/3")
#print(response.json())
