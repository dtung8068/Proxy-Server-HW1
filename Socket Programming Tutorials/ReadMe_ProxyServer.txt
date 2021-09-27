HOW TO RUN ProxyServer.py:

1. Open a Command Prompt
2. Set the file directory to this folder.
3. Type in "python ProxyServer.py", and hit Enter.
4. An IP Address and a Port Number should show up. Those can be changed if so desired in the code itself. 
5. Open a web browser.
6. In the search bar, type in "http://ipaddress:portnumber/link, where ipaddress is the IP Address, portnumber is the Port Number, and link is a desired webpage.
7. If the webpage is cached locally, the cache will be opened in the web browser. Else, the proxy server will take in the link, send its own request to the server,
send the webpage back to the browser, and then cache the webpage. 
8. Note that some features, such as images, are missing due to an inability to connect to them. 
