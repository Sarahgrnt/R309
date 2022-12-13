from client import server

host=input("hostname:")
port=int(input("port:"))
heim=server(host,port)
heim.connected()
rep = heim.send("connecté")
if rep == " ":
    print("serveur non connecté")
else:
    print(rep)