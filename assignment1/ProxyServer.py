import socket #For timeout purposes
SERVER_PORT = 8888 #Change as needed.
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #From Ex. Code
serverSocket.bind((socket.gethostname(), SERVER_PORT)) #gethostname(): Gets IP Address automatically
serverSocket.listen(1) #1 Request at a time.
print('The server is ready to receive on port ' + str(SERVER_PORT)) #Port Number to connect to. 
save_url = b""
firstTime = False #Used to store first time connecting to site.
while True:    
    print(serverSocket.getsockname()[0]); #IP Address to connect to 
    connectionSocket, addr = serverSocket.accept() 
    request = connectionSocket.recv(1024) #HTTP Request
    if(request != b''):
        temp = request.split(b'GET /')
        try:
            temp = temp[1]
        except IndexError:
            continue #This is not a GET. Don't worry about this. 
        temp = temp.split(b' HTTP/1.1') 
        url = temp[0] #Parse Str to get url.
        if(save_url == b""):
            try:
                extra_info = url.split(b'/')[1] #Extract stuff like /index.html.
                url = url.split(b'/')[0] 
            except IndexError:
                extra_info = b"" #If not found, just make it empty. 
            save_url = url
        else:
            extra_info = url #Should go here when main page loads up. 
        try:
            replace_slash = extra_info.decode().replace('/', '-') #Replace / with - as / isn't accepted by File Explorer.
            replace_slash = replace_slash.replace('?', 'q') #Replace ? with q; ? isn't accepted by File Explorer.
            file = open(save_url.decode() + replace_slash, 'rb') #If file exists, load it up (cache)
            content = file.read() 
            file.close()
            try:
                content = content.split(b'<!doctype html>')[1] 
            except IndexError:
                content = content #Sometimes, you don't have an HTML. 
            connectionSocket.send(b'HTTP/1.1 200 OK\n\n' + content) #Content should show up here.
        except (FileNotFoundError, OSError):
            clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Else, send request to webpage, and send response back to client. 
            try:
                clientSocket.connect((save_url.decode(), 80)) #Connect with website.
            except socket.gaierror:
                continue #If socket can't connect, skip. 
            request2 = 'GET /' + extra_info.decode() +  ' HTTP/1.1\r\nHost: ' + save_url.decode() + '\r\n\r\n' #Request Format. 
            clientSocket.send(request2.encode()) #Send to web server.
            clientSocket.settimeout(3) #Timeout = 3sec.
            webpage = b""#Should be the website at the end, but for now, it's blank. 
            try:
                while(True):
                    temp = clientSocket.recv(1024) #Read packets. This will hang if empty. 
                    if(len(temp) > 0):
                        webpage += temp #Add to webpage. 
                    else:
                        break
            except socket.timeout:
                print("Finished Reading") #Should go here when you can't read anymore.
            connectionSocket.send(webpage) #Send webpage back to client.
            code = webpage.split(b'HTTP/1.1 ')[1] #Just want the success code here.
            code = code.split(b'\r\n')[0]
            if(code.decode() == '200 OK'): #If webpage opens and is not a redirect, cache the contents. 
                f = open(save_url.decode() + replace_slash, "wb") 
                f.write(webpage) #Write contents here. 
                f.close()
            clientSocket.close() #Close proxy server socket. 
    connectionSocket.close() #Close Connection
    