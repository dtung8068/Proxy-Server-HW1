from socket import * #Import socket
SERVER_PORT = 6789 #Change as needed.
serverSocket = socket(AF_INET, SOCK_STREAM) #From Ex. Code
serverSocket.bind((gethostname(), SERVER_PORT)) #gethostname(): Gets IP Address automatically
serverSocket.listen(1) #1 Request at a time.
print('The server is ready to receive on port ' + str(SERVER_PORT)) #Port Number to connect to. 

while True:    
    print(serverSocket.getsockname()[0]); #IP Address to connect to 
    connectionSocket, addr = serverSocket.accept() 
    request = connectionSocket.recv(1024).decode() #HTTP Request
    if(request != ''):
        temp = request.split('GET /') 
        temp = temp[1]
        temp = temp.split(' HTTP/1.1') 
        url = temp[0] #Parse Str to get filename.
        try:
            file = open(url) #If file exists, open it.
            content = file.read()
            file.close()
            response = 'HTTP/1.1 200 OK\n\n' + content 
            connectionSocket.send(response.encode()) #Content should show up here.
        except FileNotFoundError:
            connectionSocket.send(('HTTP/1.1 404 Not Found\n\n').encode()) #Else, 404 Not Found
    connectionSocket.close() #Close Connection
    