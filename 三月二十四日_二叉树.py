import socket
def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(b"wohaocaia", ("192.168.0.112",5555))
    udp_socket.close()





if __name__ =="__main__":
    main()