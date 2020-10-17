import requests
    
valid_tokens=[]

with open("tokens.txt","r+") as f:
    for line in f:
        token=line.strip("\n")
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        request=requests.get(url,headers=headers)
        if request.status_code == 200:
            print(token+" is valid")
            valid_tokens.append(token)
        else:
            print("invalid token found "+token)
            
with open("tokens.txt","w+") as f:
    for i in valid_tokens:
        f.write(i+"\n")