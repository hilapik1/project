import select
import socket
import time
from datetime import datetime
from datetime import date

MAX_MSG_LENGTH = 1024
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP
server_socket.bind((SERVER_IP, SERVER_PORT))
server_socket.listen()
list_of_Names = []
name_count = 0
clients_socket = []
messages_to_send = []  # ( dstClient ,  data )
AddrDict = {}
type_message = []


def Calculate_Time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)
    time = current_time.split(':')
    time_update=time[0]+':'+time[1]
    return time_update
    #print(time_update)

def Calculate_Date():
    today = date.today()
    # Textual month, day and year
    d2 = today.strftime("%B %d, %Y")
    #print("d2 =", d2)
    return d2;

TosendTo = []
TosendTo1=[]
while True:

    rlist, wlist, xlist = select.select([server_socket] + clients_socket, clients_socket, [])

    for current_socket in rlist:
        if current_socket is server_socket:
            (connection, client_address) = current_socket.accept()
            print("New client joined! {} con {} ".format(client_address, connection))
            clients_socket.append(connection)
        else:
            length_mes = current_socket.recv(4)#.decode()
            if length_mes==b'':
                clients_socket.remove(current_socket)
                # if clients_socket == []:
                #     server_socket.close()
            else:
                length_mes=length_mes.decode()
                optional_msg = current_socket.recv(int(length_mes)).decode()
                type_message = optional_msg.split('$')
                if type_message[0] == "name":
                    print(type_message[1])
                    list_of_Names.append(type_message[1])
                    d = {current_socket: list_of_Names[name_count % len(list_of_Names)]}
                    print(list_of_Names[name_count % len(list_of_Names)])
                    name_count += 1
                    AddrDict.update(d)
                    print(AddrDict)
                    cur_date = Calculate_Date()
                    #current_socket.send(cur_date.encode())
                elif type_message[0] == "message":
                    if type_message[1] == "":
                        print(" Connection closed ")
                        clients_socket.remove(current_socket)
                        AddrDict.pop(current_socket)
                        current_socket.close()
                    else:
                        print(" {} >> {} ".format(AddrDict.get(current_socket), type_message[1]))
                        TosendTo = clients_socket.copy()
                        TosendTo.remove(current_socket)  # len = amount connected - 1
                        print(type(type_message[1]))
                        print(type_message[1])
                        print(type(AddrDict.get(current_socket)))
                        print(AddrDict.get(current_socket))
                        time_cur=Calculate_Time()
                        messages_to_send.append((TosendTo,time_cur +" "+ str(AddrDict.get(current_socket)) + ": " + type_message[1]))
                elif type_message[0] == "quit":
                     clients_socket.remove(current_socket)
                     # if clients_socket == []:
                     #    server_socket.close()
                elif type_message[0] == "image":
                    codelen= current_socket.recv(4)
                    code_emoji=current_socket.recv(int(codelen))
                    TosendTo1 = clients_socket.copy()
                    TosendTo1.remove(current_socket)  # len = amount connected - 1
                    for s in clients_socket:
                        if s in wlist and s != current_socket:
                            # send image message prefix
                            s.send(str("image$"+code_emoji.decode()+"$"+str(AddrDict.get(current_socket))).encode())
                            t="image$"+code_emoji.decode()
                            f=str("image$"+code_emoji.decode()+"$"+str(AddrDict.get(current_socket))).encode()
                            print(f)
                            #print(t)
                            #time.slep(0.6)
                            # send image code length
                            #s.send(codelen)
                            # send image code
                            #s.send(code_emoji)

    for message in messages_to_send:
        (SocketsToSend, data) = message
        for current_socket in SocketsToSend:
            if current_socket in wlist:
                current_socket.send("message$".encode())
                #time.sleep(0.6)
                current_socket.send(data.encode())
                SocketsToSend.remove(current_socket)
        if not SocketsToSend:  # SocketToSend is empty
            messages_to_send.remove(message)