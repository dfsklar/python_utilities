import os
import poplib
from creds import POP_LOGIN, POP_PWD, TWILIO_AUTH_TOKEN, TWILIO_ACCOUNT_SID
from twilio.rest import Client


alarm_message='''
<Response>
	<Say voice="woman">This is a robot set up by David.
We have just received a warning from the Orion water system.
Have David double-check that the go-vee application is indeed reporting unexpected water.
</Say>
</Response>
'''


def make_voice_call():
	print("about to make a voicecall via twilio - next line will be the response")
	client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
	call = client.calls.create(
                        twiml=alarm_message,
                        to='+1AAABBBCCCC',
                        from_='+1AAABBBCCCC'
                    )
	print(call)


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
	make_voice_call()
	server.dele(1)

# close pop3 server connection.
server.quit()
