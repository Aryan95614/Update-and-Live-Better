import socket
from _thread import *
from ClickForCode.C_onstants import *
from ClickForCode.client import a
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = "0"
pos = ["0:50,50", "1:100,100"]

dat = []
numTimes = 0
def threaded_client(conn):
    global currentId, pos, nid
    #conn.send(str.encode('Hall'))#str.encode(currentId))
    currentId = "1"
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                print("Recieved: " + reply)
                conn.send(str.encode(reply))
                dat.append(reply)
                print("Sent message!")
                arr = reply.split(":")




            conn.sendall(str.encode(reply))

        except:
            break

    print("Connection Closed", end = "\n")
    conn.close()
    print(numTimes)
    if numTimes == 1:
        a(dat)

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    conn.sendall(str.encode('Hall'))
    start_new_thread(threaded_client, (conn,))
    numTimes+=1