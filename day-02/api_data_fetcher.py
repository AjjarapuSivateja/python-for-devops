import requests

api_url="http://api.mediastack.com/v1/"
API_KEY = "f3f1fa3e28ebe8431cc41ad1fe3ab56d"
query=f"news?access_key={API_KEY}"
print(api_url+query)


def get_media_facts():
    response=requests.get(url=api_url+query)
    for key,value in response.json().items():
        print(key,value)
    with open("response.txt","w") as f:
        f.write(response.text)
    print("Response saved to response file")    
get_media_facts()  


