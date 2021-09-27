import socket

def main():
    global listen_port, buffer_size, max_conn
    listen_port = 8888
    buffer_size = 1024
    max_conn = 1

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((socket.gethostname(), listen_port))
        s.listen(max_conn)
        print("[*] Initializing socket....Done.")
        print("[*] Socket binded successfully...")
        print("[*] Server started successfully [{}]".format(listen_port))
    except Exception as e:
        print(e)
    while True:
        try:
            conn, addr = s.accept()
            data = conn.recv(buffer_size)
            conn_string(conn, data, addr)
        except KeyboardInterrupt:
            s.close()
            print("\n[*] Shutting down....")
        s.close()
def conn_string(conn, data, addr):
    try:
        first_line = data.split("\n")[0]
        url = first_line.split(" ")[1]
        http_pos = url.find("://")
        if http_pos == -1:
            temp = url
        else:
            temp = url[(http_pos + 3):]
        port_pos = temp.find(":")
        webserver_pos = temp.find("/")
        if webserver_pos == -1:
            webserver_pos = len(temp)
        webserver = ""
        port = -1
        if port_pos == -1 or webserver_pos < port_pos:
            port = 80
            webserver = temp[:webserver_pos]
        else:
            port = int(temp[(port_pos + 1):][:webserver_pos - port_pos - 1])
            webserver = temp[:port_pos]
        print(webserver)
        proxy_server(webserver, port, conn, data, addr)
    except Exception as e:
        print(e)
def proxy_server(webserver, port, conn, data, addr):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(data)
        while True:
            reply = s.recv(buffer_size)
            if len(reply) > 0:
                conn.send(reply)
                dar = float(len(reply))
                dar = float(dar / 1024)
                dar = "{}.3s".format(dar)
                print("[*] Request Done: {} => {} <= {}".format(addr[0], dar, webserver))
            else:
                break
        s.close()
        conn.close()
    except socket.error as value:
        s.close()
        conn.close()
main()