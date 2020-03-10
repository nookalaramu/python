import pysftp

srv = pysftp.Connection(host="www.destination.com", username="xxx",
password="xxx",log="./temp/pysftp.log")

with srv.cd('public'): #chdir to public
    srv.put('C:\Users\XXX\Dropbox\test.txt') #upload file to nodejs/

# Closes the connection
srv.close()