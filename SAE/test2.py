from client import server
import thread
import time

host1=input("host : ")
host2= input("2eme serveur")
hostsocket1=server(host1,10055)
hostsocket2=server(host2,10055)
hostsocket1.connect()
print("connection serveur")
hostsocket2.connect()
#time.sleep(2)

while not hostsocket1.isConnected():
    time.sleep(1)

print(hostsocket1.isConnected())

for i in range(10):
    hostsocket1.send("Ok")
    print(f"Ok {i}")
    hostsocket2.send("k")

hostsocket1.waitSend()
hostsocket1.close()
hostsocket2.close()

