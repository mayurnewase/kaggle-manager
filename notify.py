from twilio.rest import Client
import os

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure

class Notify():

	def __init__(self, kernel_name, notify_message, tone_path = None):
		self.account_sid = os.environ.get("account_sid") or 'ACe3a3f05697646a8d0e1771bbf69417b1'
		self.auth_token = os.environ.get("auth_token") or '30f91fc063cd0efa51c717e5174b7595'
		self.twillio_number = os.environ.get("number") or '+13054071181'
		self.personal_number = os.environ.get("personal_number") or '+919423514849'

		self.kernel_name = kernel_name
		self.notfy_message = notify_message

		self.tone_path = tone_path

	def notifyMessage(self):

		client = Client(account_sid, auth_token)

		message = client.messages \
		                .create(
		                     body = self.kernel_name + " " + self.notify_message,
		                     from_='+13054071181',
		                     to='+919423514849'
		                 )

		print(message.sid)

	def notifyLinux(self):
		os.popen(f"notify-send {self.kernel_name} {self.notify_message}")

	def notifyTone(self):
		os.system(f"ffplay {self.tone_path} -nodisp")



#to='+917020846176'
#to='+919423514849'