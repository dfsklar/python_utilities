# import python poplib module
import poplib
from creds import POP_LOGIN, POP_PWD 

# input email address, password and pop3 server domain or ip address
email = POP_LOGIN
password = POP_PWD
pop3_server = 'mail.sklardevelopment.com'

# connect to pop3 server:
server = poplib.POP3(pop3_server)
# open debug switch to print debug information between client and pop3 server.
server.set_debuglevel(1)
# get pop3 server welcome message.
pop3_server_welcome_msg = server.getwelcome().decode('utf-8')
# print out the pop3 server welcome message.
print(server.getwelcome().decode('utf-8'))

# user account authentication
server.user(email)
server.pass_(password)

# stat() function return email count and occupied disk size
(email_count, disk_size) = server.stat()

if email_count > 0:
    server.dele(0)

# close pop3 server connection.
server.quit()