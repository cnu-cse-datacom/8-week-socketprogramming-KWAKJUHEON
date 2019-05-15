import socket
import os
FLAGS = None


class ClientSocket() :

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def socket_send(self):
        print("<< SENDING START >>\n")
        ID = input("input your file name : ")
        count = 0

#        check1 = ID[len(ID)-1]
#        check2 = ID[len(ID)-2]
#        check3 = ID[len(ID)-3]
#        check = check3 + check2 + check1
#        print(check)
        self.sock.sendto(str(ID).encode(), (FLAGS.ip,FLAGS.port))
        f = open(ID,"rb")
        total_size = os.path.getsize(ID)
        print("your file size : ", total_size, "\n")
        self.sock.sendto(str(total_size).encode(), (FLAGS.ip, FLAGS.port))
        current_size = 0
        l = f.read(1024)
        while l:
#             if check == "txt": 
#                  l = l.decode()
#                  current_size = self.sock.sendto(l.encode(), (FLAGS.ip, FLAGS.port))
#                  print(l, "-- current sending rate : ", 100*(current_size / total_size), "%")
    

             current_size += self.sock.sendto(l, (FLAGS.ip, FLAGS.port))
#             print(current_size)
             print("-- current sending rate : ", current_size, " / ", total_size, "= ", 100*(current_size / total_size), "%")
             l = f.read(1024)
        self.sock.sendto("send complete!!".encode(), (FLAGS.ip, FLAGS.port))   
        print("\n<< SENDING END >>")
          
        f.close() 
        self.sock.close()
     
    def main(self):
        self.socket_send()
if __name__ == '__main__':
        import argparse

        parser = argparse.ArgumentParser()
        parser.add_argument('-i', '--ip', type=str, default = 'localhost')
        parser.add_argument('-p', '--port', type=int, default = 8080)

        FLAGS, _ = parser.parse_known_args()

        client_socket = ClientSocket()
        client_socket.main()
