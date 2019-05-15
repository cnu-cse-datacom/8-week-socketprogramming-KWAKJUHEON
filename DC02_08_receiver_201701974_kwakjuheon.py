import socket
import os
from time import sleep

FLAGS = None

class ServerSocket() :
      def __init__(self):
          self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
          self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
          self.server_socket.bind((FLAGS.ip, FLAGS.port))

      def socket_receive(self):
#          server_socket.bind((FLAGS.ip, FLAGS.port))
          print("<< RECEIVING START >>\n")
          count = 0
          total_size = 0
          current_size = 0
          file_name = ""
          while True:
                 data, addr = self.server_socket.recvfrom(1024)
                 
                 if data == b'send complete!!':
                       break
#                if data.decode() == "send complete!!":
#                       break
#                if data.decode() == "jpg":
#                       while data:
#                           data, addr = server_socket.recvfrom(1024)
#                           print(data)
#                           f.write(data)
#                if data.decode() == "txt":
#                       while data:
#                           data, addr = server_socket.recvfrom(1024)
#                           data_check = data.decode()
#                           if data_check == "send complete!!":
#                                break
#                           print(data_check)
#                           f.write(data)

                 if count is 0:
                      count += 1
                      file_name = data.decode()
                      print("received file name : ", file_name)
                      f = open(file_name, "wb")
                      continue
                 elif count is 1:
                      count += 1
                      total_size = int(data.decode())
                      print("file total size : ", total_size, "\n")
                      continue
                 elif count > 1: 
#                     print(count)
                      f.write(data)
                      current_size += len(data)
#                     print(current_size)
                      print("-- current receiving rate : ", current_size, "/", total_size, " = ", 100*(current_size/total_size), "%")
#                 if 100*(current_size / total_size) == 100.0:
#                      break
      
            
          print("\n<< RECEIVING END >>")
          f.close()
          self.server_socket.close()

      def main(self):
          self.socket_receive()

if __name__ == '__main__':
          import argparse

          parser = argparse.ArgumentParser()
          parser.add_argument('-i', '--ip', type=str, default = 'localhost')
          parser.add_argument('-p', '--port', type=int, default = 8080)

          FLAGS, _ = parser.parse_known_args()
          
          server_socket = ServerSocket()
          server_socket.main()
