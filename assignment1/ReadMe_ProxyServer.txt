HOW TO RUN ProxyServer.py:

1. Open a Command Prompt
2. Set the file directory to this folder.
3. Type in "python ProxyServer.py", and hit Enter.
4. An IP Address and a Port Number should show up. Those can be changed if so desired in the code itself. 
5. Open a web browser.
6. In the search bar, type in "http://ipaddress:portnumber/link, where ipaddress is the IP Address, portnumber is the Port Number, and link is a desired webpage.
7. If the webpage is cached locally, the cache will be opened in the web browser. Else, the proxy server will take in the link, send its own request to the server,
send the webpage back to the browser, and then cache the webpage/all files attached to it. 
8. Limitations:
A. You cannot connect to multiple sites in the same server run. This is due to a variable that is used to save the original site that acts as the host.
B. The cached version of the site is missing some features, such as images. 
C. Browser specific Proxy Settings will not work with this server. 
9. List of websites that have been tested and will return a 200:
www.google.com
www.example.org
www.owgr.com (Incomplete, but text is there).
Many other sites will work, such as www.amazon.com, www.yahoo.com or the two test webpages on Piazza, but will instead return a 301. 
10. Two photographs are attached: one showing www.google.com being loaded for the first time, and the other showing www.google.com being loaded from cache. 